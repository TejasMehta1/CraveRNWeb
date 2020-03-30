# CraveRN

CraveRN is a web application designed to help users find where to satisfy 
their cravings instantly. The application allows the user to either search 
what they desire or take a short quiz to help them find exactly what they want.
The quiz is comprised of picking one out of four pictures for a few rounds. The
service then calls Yelp's Fusion 360 API and returns results matching the user's 
preferences along with a map of where the restaurants are located.

## Usage

https://craverightnow.com/
<br />
Note that this application uses IP addresses to find location, 
so the application may not work as expected when using different VPNs, proxies, etc. 

The application has been designed to work primarily with computers but has been optimised
to work with mobile phones and tablets as well, although some lines may overflow slightly. 


## Architecture

The application is designed with a Flask/Python backend and a HTML/CSS/JavaScript
frontend. The application is deployed using Google Cloud's Cloud Run. Data is stored
Google Firebase's Realtime database service. Static CSS and images are stored in a 
Google Cloud Storage bucket. 
![Architecture](https://lh3.googleusercontent.com/XTzpmLh63e1sA1nZIRl4sNeD_Hiv4fQ4kT0_F3Kr654v7wVv3BqR0hECnZMdCa2al5J0tIfFAfnFdQMk-cOfCw4Z1sKVsm1ieft2lWYirfqVhc3ByO8Yj4UlKPpLYq5D7s-K01skexslOuba5K6iViPskfyhKH17GXtHXO3iRRvkhrhgFoy7Al0s-ASacoROl_34XbN7OE7pW7Y9-gKCG01ijho3AujjT-h1t7ZRchmNWyYfYBzfkotnJ3xtvi10rpAGOv3AtF6epH47F0K4y_Tkksb_K7kfGu1rJWfpQm12N8ZrMnATyjBWIKVI_tX9JhAeaF-XhulvJLsjEQvvzgiWx-Gwuk1Qk-OJ9f3BjQCwNU90_XzHWJ4CA4UuSzGkoa1LxWlRPeAufZx3boKHuvbcPdolbbrh65Q5kHEJJOkExIXiqLIOsDajx9qftmLmbykFcPtkYvXTV8V1Krd6sbsK9jO1UnOCa4H4Awqp3ht2LkM2LqyBjQcmreff2-cSG42qU0dyYDD2Ibw66NLZp5FcJmHHvIGebUecsWfrz-cD-jTp0QQgh9l_7IzHoYuEwKIuKSDwaG0qbYlCFS5x64M0MyLPZi92VaUNo2uMPLTIoGjT-scJwcsFE31PDM_DGCprIwzvCC69QP5S9a9qGCBoJ-uszm89JkVXbcBLsS1RcnNAJQa_iwjw=w681-h501-no)

## Front End Pages

### Home: 

[home.html](server/src/templates/home.html) [home.css](server/src/templates/static/css/home.css) 
<br />
The user has two options to search. They can either enter input into the search box or they can complete the quiz
by clicking one of the four pictures until the quiz is over.
![Home Page](https://lh3.googleusercontent.com/hw13bgDlmcbGtdHLflwYOIGe54Yc5P9mUXIYX6xuJVOWirlrYKaYPIPHGs-YOGVD_DnpJL2NA1jsxgv-QEE6kOh3ETXZL3e1vbFjkiJusatgOkeGDbVIWAsURW2novWgOq-I-i7udGmZF_RiWYZNIbjeUXmtE8jSSSsaVFXkoTZc4reDSn2iP5ZljpC-rXGxxgLbG5J1bRuFUBzwgdaaE50wDYuNmwJeQTsq7nA-OnwWG9S_ygtKC4kgiRwrJJ-Ed_EjT2ayxYdjOeGNhEXUrJ9DpBTj1g042OySAt3aIDwSHeJssZyV2D3_zSQBqTApegWU3bO4eFhTlu0wGCSvihyhFJ8Bt-AfZk1p6L1UQj5VNEAUoiFJRrEiuNp3tvJsWNtAGxTjvhPPXUAOntfyFSOds8c2_L2TQYoL9ycLKGVTkRQlF96JZuzF_5HHMuAE7PZ-igPwtpOQfxeuiVj9oUH694_pFPJN-aPoPz5uxgUvA_LDvAlzQ8ObDh6IL24RmyX0HOKuFmx5fZZ1ADnQSIR4f8aBtuxDJjn5cFRm5OudHo9KUKlOFBKb3e3gBSX-FdA_LlUy_ho3RzX__cF0OnUJZpVjfIk8_fK0GTOauILhMVIpODCLy8jVM4fpYPCfC7ROJ1UQl-N9F57nK0BT6qOlwf0is2mS3iR64SSD-nF9N0mIew2-TK4l=w3584-h2080-no)

### Results:
[results.html](server/src/templates/results.html) [results.css](server/src/templates/static/css/results.css) 
<br />
The user is displayed a scrollable list of restaurant results on the left. On the right, the user is displayed a fixed,
zoomable map with the locations of the results. The numbers on the markers correspond to the numbers labeled next to the restaurant
name on the left panel. There are three filters that can be modified to show different results on the top labeled distance, price, and sort by.
The Google Maps JavaScript api is used to create the map.
![Results](https://lh3.googleusercontent.com/cb6ATPzO4epBrkAGVF6JGrcJ6mN7DE6eYovXdEIHs5Gc80pwmQNQH8Uecu6lY7UZ1BSOPHhVU_tHkxgCMeTPGnofYOTLsckoMm7KJFiNBkG9Znj2gYhOOl0_SgyiA_GSXhXQKz_YUt-JEXJAVPTQRUlXHKqDlKG_ivBuqdNzJcsBCyPptSNJD3hcS3njtukeyuna4xZzNpGagEnHwCMivo7msUtIQoMTZnbXZvJKaeCnkFZGqZxcvhXf-KJ7P8ekdtbn0szkmp2WDBnjBa1SdEd0izoXshRPlj-C2e0OPqVmjgEr34Vgqm_cwbUhP2ebwv_xEEG3cMP8h1vlik5Px_AYT5uNmJ1ZNiFRtaQILu0iuyBvqvJemTQupqiP0bPGXVuJECxk4afRwi2yqVmRHin5lEk1FnMVEbplYXr7mP3sz0RwB3u3-xRFJh7SnXSHmyvcRFkBL3qoXLlfK6xBOJYfeFepKjxwisI9fStfbQGcKGtWOpPrvKQ1LYeCUrP4VaBEsMtAzI2zVtRI25BF-LGoSp9OG-YTLPHChRXuwRq84S7kh7DTZxfel4xVBr1k-8LMwKliYOsYx0C2dHEVAsnxzr5LMBig6nEmi5Zk8k_nLQ3dCVisEQd0UnrO7U4Oa5ohfLhII02Yhh4ePtvEQns5YgJX3E5RBnyIywiLU3il38lFbmPgrzGY=w3584-h2080-no)

I learned how to render the Google Maps view to fit the markers from https://developers.google.com/maps/documentation/javascript/adding-a-google-map?hl=ru and https://github.com/fullstackreact/google-maps-react/issues/63

I used code from: https://codepen.io/Bluetidepro/pen/GkpEa for the star ratings.

## Back End
I used a Python/Flask backend for this project. The backend is called upon two endpoints.
The code can be found in: [app.py](server/src/app.py). 
### / (Home)
The primary purpose of the home endpoint is to get the user's location, and then render
the home.html template. To get the user's location, I forked a simple port of Flask GEOIP from here:
https://github.com/whois-api-llc/flask-simple-geoip/blob/master/flask_simple_geoip.py.
The key difference in my api and theirs is that theirs uses the request.remote_addr attribute to get the ip address
and mine takes the IP address as a parameter. Since I'm hosting on Google Cloud Run, remote_addr gets a private IP not correlated to
the user's actual IP address. In order to get the user's actual IP address, I used the request.environ['HTTP_X_FORWARDED_FOR'] attribute in the app.py file.
This is why the page throws an error if the backend does not recieve a valid public IP (VPN, Proxy, etc). I am currently looking for workarounds for this problem
like getting the user's location in the frontend using HTML5 Geolocation. 

My forked API can be found here: [flask_simple_geoip_TejasFork.py](server/src/TejasGeoIPFork/flask_simple_geoip_TejasFork.py)


 Initialization: ```GeoIP1 = TejasGeoIP(app)```
 
 Utilization: ```geoip_data = GeoIP1.get_geoip_data(ip)```

 (app: your flask instance, ip: IP address)
### /results
The results endpoint is called by home.html after the user either enters a text query or 
completes the four picture quiz. The endpoint expects the following parameters: 
* typeOfMeal
* specificMeal
* restaurantType
* dietaryRestriction
* latitude
* longitude
* city
* state
* price
* distance
* sort_by

The typeOfMeal, restaurantType, dietaryRestriction, price, and distance can have a "null" value.

The endpoint takes these queries, processes them in a way that the Yelp Fusion API can understand, and returns the output
from the api to the results.html document. I pass in the open_now parameter to be true so it only results in restaurants currently
open. 

## Deployment
The script I created to deploy the app is found here: [deployToCloudAndFirebase.sh](server/deployToCloudAndFirebase.sh)

### Google Cloud Run:
The application is hosted by a Google Cloud Machine through the Google Cloud Run 
service. The Cloud Run service uses the dockerfile here: [Dockerfile](server/Dockerfile) to create a container
to host the service. The dockerfile instructs the machine to install the python libraries I used using pip and uses
the Gunicorn WSGI application server to allow the flask app to communicate with the web server.

I learned how to host using google cloud run using this tutorial: 
https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run

### Google Firebase Realtime Database:
The core logic for the pictures that should show up and what order they should show up for the four picture quiz in the homepage
is dictated by the data in the realtime database. Each phase has different possible picture labels detailed in the database. Some phases will have
different pictures that need to be shown based off of the previous answer. The database effectively works like a mix between a linked list and a tree.
The database also has the urls for each image with the image label as the key. 
The data can be seen below or here: [choiceTree.json](choiceTree.json)
```{
  "URLS" : {
    "1" : "https://storage.googleapis.com/cravern/static/img/1.jpg",
    "2" : "https://storage.googleapis.com/cravern/static/img/2.jpg",
    "3" : "https://storage.googleapis.com/cravern/static/img/3.jpg",
    "4" : "https://storage.googleapis.com/cravern/static/img/4.jpg",
    "10mi" : "https://storage.googleapis.com/cravern/static/img/10mi.jpg",
    "1mi" : "https://storage.googleapis.com/cravern/static/img/1mi.jpg",
    "20mi" : "https://storage.googleapis.com/cravern/static/img/20mi.jpg",
    "5mi" : "https://storage.googleapis.com/cravern/static/img/5mi.jpg",
    "alcohol" : "https://storage.googleapis.com/cravern/static/img/alcohol.jpg",
    "anything" : "https://storage.googleapis.com/cravern/static/img/anything.jpg",
    "appetizer" : "https://storage.googleapis.com/cravern/static/img/appetizer.jpg",
    "asian" : "https://storage.googleapis.com/cravern/static/img/asian.jpg",
    "boba" : "https://storage.googleapis.com/cravern/static/img/boba.jpg",
    "buffets" : "https://storage.googleapis.com/cravern/static/img/buffets.jpg",
    "cake" : "https://storage.googleapis.com/cravern/static/img/cake.jpg",
    "casual" : "https://storage.googleapis.com/cravern/static/img/casual.jpg",
    "chips" : "https://storage.googleapis.com/cravern/static/img/chips.jpg",
    "coffee" : "https://storage.googleapis.com/cravern/static/img/coffee.jpg",
    "cookies" : "https://storage.googleapis.com/cravern/static/img/cookies.jpg",
    "dessert" : "https://storage.googleapis.com/cravern/static/img/dessert.jpg",
    "doughnut" : "https://storage.googleapis.com/cravern/static/img/doughnut.jpg",
    "drinks" : "https://storage.googleapis.com/cravern/static/img/drinks.jpg",
    "dumplings" : "https://storage.googleapis.com/cravern/static/img/dumplings.jpg",
    "fastFood" : "https://storage.googleapis.com/cravern/static/img/fastFood.jpg",
    "foodTruck" : "https://storage.googleapis.com/cravern/static/img/foodTruck.jpg",
    "friedSnacks" : "https://storage.googleapis.com/cravern/static/img/friedSnacks.jpg",
    "glutenFree" : "https://storage.googleapis.com/cravern/static/img/glutenFree.jpg",
    "healthy" : "https://storage.googleapis.com/cravern/static/img/healthy.jpg",
    "iceCream" : "https://storage.googleapis.com/cravern/static/img/iceCream.jpg",
    "indian" : "https://storage.googleapis.com/cravern/static/img/indian.jpg",
    "italian" : "https://storage.googleapis.com/cravern/static/img/italian.jpg",
    "juice" : "https://storage.googleapis.com/cravern/static/img/juice.jpg",
    "mainDish" : "https://storage.googleapis.com/cravern/static/img/mainDish.jpg",
    "mexican" : "https://storage.googleapis.com/cravern/static/img/mexican.jpg",
    "milkshake" : "https://storage.googleapis.com/cravern/static/img/milkshake.jpg",
    "none" : "https://storage.googleapis.com/cravern/static/img/none.jpg",
    "premium" : "https://storage.googleapis.com/cravern/static/img/premium.jpg",
    "tapas" : "https://storage.googleapis.com/cravern/static/img/tapas.jpg",
    "vegan" : "https://storage.googleapis.com/cravern/static/img/vegan.jpg"
  },
  "round1" : [ "dessert", "appetizer", "mainDish", "drinks" ],
  "round2" : {
    "appetizer" : [ "chips", "dumplings", "tapas", "friedSnacks" ],
    "dessert" : [ "iceCream", "cookies", "cake", "doughnut" ],
    "drinks" : [ "alcohol", "boba", "juice", "coffee" ],
    "mainDish" : [ "italian", "indian", "asian", "mexican" ]
  },
  "round3" : [ "1", "2", "3", "4" ],
  "round4" : [ "foodTruck", "fastFood", "buffets", "anything" ],
  "round5" : [ "healthy", "glutenFree", "vegan", "none" ],
  "round6" : [ "1mi", "5mi", "10mi", "20mi" ]
}
```

### Static File Hosting:
In order to allow my HTML to access my static file (images and css), I hosted these files
using Google Cloud storage buckets. In my deployment script, I upload all of the files in my static folder
here: [choiceTree.json](server/src/templates/static) to a bucket in Google cloud storage. 

I learned how to do this using this link: https://cloud.google.com/storage/docs/hosting-static-website
