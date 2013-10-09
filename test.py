import urllib
import oauth2
import time
import json

def build_request(url, method='GET'):

	params = {
		'oauth_version': "1.0",
		'oauth_nonce': oauth2.generate_nonce(),
		'oauth_timestamp': int(time.time()),
		'keywords': 'NFL,cheerleader',
		'mode': 'phrase',
	}
	consumer = oauth2.Consumer(key='duckfat',secret='3xpr355way')
	params['oauth_consumer_key'] = consumer.key

	req = oauth2.Request(method=method, url=url, parameters=params)
	signature_method = oauth2.SignatureMethod_HMAC_SHA1()
	req.sign_request(signature_method, consumer, None)
	return req


request = build_request('http://www.usatodaysportsimages.com/api/searchAPI/')
u = urllib.urlopen(request.to_url())
data = u.read()

jsondata = json.loads(data)
print json.dumps(jsondata, indent = 4)
print request.to_url()
