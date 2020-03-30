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
![Architecture](https://lh3.googleusercontent.com/U_-078MMZJYMorCIZDt1eG1wBuxR37NySxlRdrlark4FSt54djjoV_qcDFFcnWsdwf_W-mbqExXId6iPJtW33yRvtUze5GCTLu6JFV-0CMavUYvEQPjfSkZur96YJyDQ22v1yQeFNp59w6Afv3em_KPqQI7sBrDpTCzd-NE_9M7bSYrtR3_NKdF9uu5O_6yzO_Ka-aB2OYyUNgMvJiFHeLKVKU5NW4-2fsKdIc341sRDoxcLZ--VZ99JX5NluhkEyYo2dz6AHG6JtqihLYSI7pf4ivZyQ0BxfeqTqYUjpScDbrOMgqlLV1pVJXtIaua8QMmj64JdDPlyR-J_s9kEmdIyQcow-UtXM5ITm4lbSsBB2Hl2HGWljjHG1kAh5qPc4FOpJUYpFm_mXmdiU-V3Ey-alNwthEMcObdeIgD2r1oPZ4YOGj2HRPjTXuD_GqmhAg3YgKhCsJbU-j2Ewb75ho2rDukcHaVVGM27614vRoBp7VCuhSAv1w_9L2UnxWnYA1svYiIuCJvWqIP01ZWZoWcvnaNtHtM4MxF80h1xWtLMUqLi1wJik6itpkzB300aC6kFGJfGc77p-fvZW0wz-ZOiBTgm42Rprib_Nw5x1pQV2XVatHaaL7p3AAQ3BmpJWzF34tnjA43e7gCeATH82aAqC03S2SwHWMX9jLtTYvigUZpo3mEuVlNpZ4cLhjTpyONG=s681-w681-h501-no)

## Front End Pages

### Home: 

[home.html](server/src/templates/home.html) [home.css](server/src/templates/static/css/home.css) 
<br />
The user has two options to search. They can either enter input into the search box or they can complete the quiz
by clicking one of the four pictures until the quiz is over.
![Home Page](https://lh3.googleusercontent.com/FVhlClRoIllWXxHC7iz3gwzxwh8a7ohmw06Nz-YgjdWpkf8d4_aW7MsLxSbOQ89CuK1l1uXL3LDjLxu4LqrQ-jvor8k-Yimnjw5RCjoq5hybOf3WaK7S4bHZMVeRSMcqh7_TV8-pAWvVvvap818efRObU-z0JavU2PLKstXkstSjAmDQ2B7ZU_hAECOhObrJ-27_p2tEtfRCWw5AdapBvEHtkc12-Ztm9vCLcvXkd3_iVkVoqhkAeJ9DCl0Nr6djE567HWO_ghzwF1K6c-HkEFiGMXN9IgJjo1ZYYmhgZR41fZRZsUEXKGYiQ1nto56rq56Nx3zXK8LSoBYt0PKDdWKFn6wGkvYeUsE39JQ_WgrWf4_AfTIEcCrOPvtcx6WBBSWsiiZuBaNAKEtXLJPF33Hddj3lmL9zNn11wcyAAHtpy1JS6QI1QPDDr9s_Qk9KgnI6pkJnME_ZYHoLm83dGsgc3uwSLXfSp524w-QC9QLW-kh1g3qAw7dEYZ_Fja-L3mz9-AAN2uXeeioXMle6ztGSgY3NyvZvHV216iVEBD2cxZ_LW5xnroTm9-y7DD1r61pueiJqhjAsK28vleuFev_Ry2cCRzZObaPXNHBlkDMZcel4ZUGcB2kXW3iwhAlfqDz1o66UMl-QfoEi9SVObRXwJXdNqca9k9lGVVsT8l62mDBwqIT8tI5X-TTeDyOgvd-Z=s3584-w3584-h2080-no)

### Results:
[results.html](server/src/templates/results.html) [results.css](server/src/templates/static/css/results.css) 
<br />
The user is displayed a scrollable list of restaurant results on the left. On the right, the user is displayed a fixed,
zoomable map with the locations of the results. The numbers on the markers correspond to the numbers labeled next to the restaurant
name on the left panel. There are three filters that can be modified to show different results on the top labeled distance, price, and sort by.
The Google Maps JavaScript api is used to create the map.
![Results](https://lh3.googleusercontent.com/PrYsKR-m6a09TVDh6DgPlwfvmZ3cH_CnxBd0SKL7I1sKt-XORHXXXgauOecsbN4OBg_TqVHH03mHnqQD9ykswft6jlskuGwszxJn6rr2BAo3DL0tPYzcpQUeZxGXjuiqhOC-wgzEuTgfu7toJOfYMPNwy3UK9XBpUAhZx3Pis8kU0AVbYYS0sh0Eksjj5tMle0oHMpDbUemNaSKQ73_-WOFYJahRs4xJ6xxT0_Ij7DoI8_uOL9dyYHbxvu2nt1vzM9XVHxYRCatv70i2MZyrPZpvaqg4ZU4Bnjsjm84dOlubwBUqIppgVt18M7l1ZNb4Zc6chnf1bFjbr4J289AwuU-wgGVJhK1FK4Sz9thd3UGwNkYu4-DAjC7pGlf-GQDIizJ3Utqy2yhKV-KdXpph0pp1mQSFa29ir5qpXooNpLnURZXzVLL-EuEYvqTp9QtepNoHsrF-BzRd7r16wlXRtHoE6YGt_NC1UK74QAZYhi9vcHvMHr91vZoQloBgEImcilMB-W-46Hq48mpn38jiyH6f7_9dqct9QfyejY6TfBEISj2HzcofDpyH9xFS4Hn6wfLGhXTQqCATmnscwCKy-yS4ZM49KP-TIp6gQFt4DZ0ICO4dirY-utG3DkXCxANWG09bIF5ljxXNsPT3aA6XxOnO02_L5RZVNzfIjXILebY0B4OTobdkOlZi6WpvjA5B5xdZ=s3584-w3584-h2080-no)

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
