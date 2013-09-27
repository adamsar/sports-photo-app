"""
Image API interaction library
"""

from photos.util import urls
from photos.util import oauth

import settings
import simplejson

import urllib
import urllib2
import StringIO
import logging

log = logging.getLogger(__name__)

class BlankRequest(object):

    def to_url(__self__):
        raise TypeError("Request not explicitly set yet")
        

class ImageApi(object):

    
    def __init__(self, key=settings.SPORTS_API['key'],
                 secret=settings.SPORTS_API['key']):
        """
        Bootstrap ourselves with a request
        """
        self.key = key
        self.secret = secret
        self.request = BlankRequest()


    def request(self, params={}):
        self.request = oauth.build_request(urls.API_ENDPOINT,
                                           self.key,
                                           self.secret,
                                           params=params)

    def list(self):
        url = self.request.to_url()
        log.debug("Calling out to {}".format(url))
        response = urllib.urlopen(url)
        log.debug("Results: {}".format(response))        
        results = simplejson.loads(response)
        return results

        
    def download(self):
        url = self.request.to_url()
        log.debug("Downloading from {}".format(url))
        raw_image = urllib2.urlopen(url).read()
        log.debug("Downloaded")
        return raw_image
        
