from photoapp import settings
from photos.api import oauth
from photos.api.results import ImageResults
from photos.util.decorators import generative

import json
import urllib
import urllib2

import logging
log = logging.getLogger(__name__)

API_ENDPOINT = "http://www.usatodaysportsimages.com/api/searchAPI/"

class BlankRequest(object):
    """
    An unformed request that will error out when
    trying to deal with it
    """

    def to_url(__self__):
        raise TypeError("Request not explicitly set yet")



class ImageApi(object):
    
    def __init__(self, key=settings.SPORTS_API['key'],
                 secret=settings.SPORTS_API['secret']):
        """
        Bootstrap ourselves with a request
        """
        self.key = key
        self.secret = secret
        self.request = BlankRequest()


    @generative
    def make_request(self, params={}):
        self.request = oauth.build_request(API_ENDPOINT,
                                           self.key,
                                           self.secret,
                                           params=params)

    def list(self):
        url = self.request.to_url()
        log.debug("Calling out to {}".format(url))
        response = urllib.urlopen(url).read()
        log.debug("Results: {}".format(response))
        results = json.loads(response)        
        return ImageResults(results)

    def one(self):
        """
        Returns the first result from the API.
        """
        return self.list().items[0]
    
        
    def download(self):
        url = self.request.to_url()
        log.debug("Downloading from {}".format(url))
        raw_image = urllib2.urlopen(url).read()
        log.debug("Downloaded")
        return raw_image
