import oauth2
import time

import logging
log = logging.getLogger(__name__)

SIGNATURE_METHOD = oauth2.SignatureMethod_HMAC_SHA1()
OAUTH_VERSION = '1.0'

def blank_request_params():
    return {
        'oauth_version': OAUTH_VERSION,
        'oauth_nonce': oauth2.generate_nonce(),
        'oauth_timestamp': int(time.time())
    }


def build_request(url, key, secret, method='GET', params={}):
    consumer = oauth2.Consumer(key=key, secret=secret)
    params.update({'oauth_consumer_key': consumer.key})
    params.update(blank_request_params())
    request = oauth2.Request(method=method, url=url, parameters=params)
    request.sign_request(SIGNATURE_METHOD, consumer, None)
    log.debug("Built request: {}".format(request))
    return request
