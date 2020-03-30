# I forked a simple port of Flask GEOIP from here:
# https://github.com/whois-api-llc/flask-simple-geoip/blob/master/flask_simple_geoip.py

# The key difference in my api and theirs is that theirs uses the request.remote_addr attribute to get
# the ip address and mine takes the IP address as a parameter.

# Since I'm hosting on Google Cloud Run, remote_addr gets a private IP not correlated to
# the user's actual IP address. In order to get the user's actual IP address, I used the
# request.environ['HTTP_X_FORWARDED_FOR'] attribute in the app.py file.

# Initialize: GeoIP1 = TejasGeoIP(app)
# Utilization: geoip_data = GeoIP1.get_geoip_data(ip)
# app: you flask instance
# ip: IP address


from os import environ

from simple_geoip import GeoIP
from flask import request

# Pass in API Key as arg: "GEOIPIFY_API_KEY"
CONFIG_KEY = "GEOIPIFY_API_KEY"

class SimpleGeoIP(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

# Check for API Key being passed in
    def init_app(self, app):
        api_key = app.config.get(CONFIG_KEY) or environ.get(CONFIG_KEY)
        if not api_key:
            raise Exception("No API key was supplied for performing GeoIP lookups. Please set a value for GEOIPIFY_API_KEY.")
        self.geoip_client = GeoIP(api_key)


# ip is the ip address parameter passed in by the caller
    def get_geoip_data(self,ip):
        """
        Performs a geoip lookup based on the requester's public IP address.
        NOTE: This method will *always* return and never raise an exception --
        it does this strategically because performing a geoip lookup should
        never be a tier 1 stop-the-world exception.
        :rtype: dict or None
        :returns: A dictionary containing the user's geolocation data, or None
            if there was a problem.
        """
        try:
            data = self.geoip_client.lookup(ip)

        # Don't do anything if an exception arises -- since geolocation data isn't
        # critical to a request being processed, we can always skip it in the worst
        # case scenario.
        #
        # By default, the underlying `simple_geoip` library will handle retry logic
        # for us ;)
        except:
            data = None

        return data