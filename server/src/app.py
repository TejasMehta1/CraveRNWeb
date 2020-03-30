import os
import ast
from flask import Flask, render_template, request, jsonify
import sys
import requests
import json

# Import Forked API
sys.path.append(os.path.abspath('./server/src/flask_simple_geoip_TejasFork.py'))
from TejasGeoIPFork.flask_simple_geoip_TejasFork import SimpleGeoIP as TejasGeoIP

app = Flask(__name__)

# API KEY FOR GEOIPIFY
app.config['GEOIPIFY_API_KEY'] = "at_ByhHYIz8uZVehC8RQqncDF7saFYw3"

# Initialize Geocoding
GEOIPIFY_API_KEY = "at_ByhHYIz8uZVehC8RQqncDF7saFYw3"
GeoIP1 = TejasGeoIP(app)

# Dictionary for Yelp's Categories to match my categories
Categories = {
    "foodTruck": "foodtrucks",
    "fastFood": "hotdogs",
    "buffets": "buffets",
    "anything": "null",
    "healthy": "healthmarkets",
    "glutenFree": "gluten_free",
    "vegan": "vegan",
    "none": "null",
    "null": "null"
}


# Home Page
@app.route('/')
def home():
    # Get IP Address from the client
    # Does not work if user is using VPN TODO Find workaround for VPN
    ip = request.environ['HTTP_X_FORWARDED_FOR']

    # Get IP Address for local testing
    # ip = request.remote_addr

    # Get Location data based off of IP Address
    geoip_data = GeoIP1.get_geoip_data(ip)
    print(geoip_data)

    # Save Location attributes
    latitude = geoip_data["location"]["lat"]
    longitude = geoip_data["location"]["lng"]
    city = geoip_data["location"]["city"]
    state = geoip_data["location"]["region"]

    # Render Homepage
    return render_template('home.html', latitude=latitude, longitude=longitude, city=city, state=state)


# Homepage with restaurant results. Only the Get endpoint is supported right now.
@app.route('/results', methods=['GET', 'POST'])
def get_results():
    if request.method == 'GET':  # Get endpoint (User types URL)
        # YELP FUSION API Url
        url = "https://api.yelp.com/v3/businesses/search?"

        # Dictionary with parameters to send to API
        params = {}

        # String to store the comma delimited categories to send to API
        categoriesParam = ""

        # Fill the categories param with restaurant type and dietary restrictions
        restaurantType = request.args['restaurantType']
        restaurantTypeCategory = Categories[restaurantType]
        dietaryRestriction = request.args['dietaryRestriction']
        dietaryRestrictionCategory = Categories[dietaryRestriction]
        if restaurantTypeCategory != "null":
            categoriesParam = (restaurantTypeCategory + ", ")
        if dietaryRestrictionCategory != "null":
            categoriesParam += dietaryRestrictionCategory
        if categoriesParam != "":
            params['categories'] = categoriesParam

        # Fill location based params
        params['latitude'] = request.args['latitude']
        params['longitude'] = request.args['longitude']

        # Get the distance in miles, convert to meters, and pass as param
        distanceInMiles = request.args['distance']
        distanceInMilesNum = 10
        if distanceInMiles != "null":
            distanceInMilesNum = distanceInMiles[0:len(distanceInMiles) - 2]
            radiusMeters = float(distanceInMilesNum) * 1609.34
            radiusIntMeters = int(radiusMeters)
            params['radius'] = radiusIntMeters

        # Default all restaurants to be open right now (Design Feature)
        params['open_now'] = 'true'

        # Fill the term parameter to be the specific meal they crave
        params['term'] = request.args['specificMeal']

        # Add price and sortBy params
        price = request.args['price']
        if price != "null":
            params['price'] = price
        sortBy = request.args['sort_by']
        if sortBy != "null":
            params['sort_by'] = sortBy

        # Sample Setup of params:
        # params = {
        #     'latitude': request.args['latitude'],
        #     'longitude': request.args['longitude'],
        #     'term': request.args['specificMeal'],
        #     # 'categories': 'delis, pizza',
        #     'radius': radiusInt,
        #     'open_now': 'true',
        #     'price:': request.args['price']
        #     # ,
        #     # 'sort_by': 'distance'
        # }

        # Add API Key as a header to allow API Use. Use Bearer auth.
        headers = {
            'Authorization': 'Bearer caG4VhMLCDUGOCbqmyejaYFDwSTE0SkB64SVd76qVtosL2H2WE9MuWqY6vePhsjh-LLwtnO4XEMwbar9uJr2uXSURmRMwtJGRW3ubDB30gZ1h2LCkkKrdhnXUAFTXnYx'
        }

        # Call the API and get return json
        response = requests.request("GET", url, headers=headers, params=params)
        print(response.text.encode('utf8'))
        jsonData = json.dumps(json.loads(response.text))

        # Render the results while passing in the return json from the API
        return render_template('results.html', results=jsonData, radiusMiles=distanceInMilesNum)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
