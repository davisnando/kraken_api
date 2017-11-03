""" Kraken Api """
import base64
import hashlib
import hmac
import json
import time
import urllib

import requests


class Krakenapi:
    """ Class to use the kraken api """

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def private_request(self, url, payload):
        """ send a request with api_key to get private data """
        payload['nonce'] = int(time.time())
        sign = self.encode_secret_key(payload, url, self.secret_key)
        headers = {
            'API-Sign': sign,
            'API-Key': self.api_key
            }

        response = requests.post(
            "https://api.kraken.com" + url,
            data=payload,
            headers=headers
        )
        return json.loads(response.text)

    def public_request(self, url, payload):
        """ send a request with api_key to get private data """
        response = requests.post(
            "https://api.kraken.com" + url,
            data=payload
        )
        return json.loads(response.text)

    def encode_secret_key(self, data, urlpath, secret_key):
        """ encode secret key """
        postdata = urllib.parse.urlencode(data)

        # Unicode-objects must be encoded before hashing
        encoded = (str(data['nonce']) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()

        signature = hmac.new(base64.b64decode(secret_key),
                             message,
                             hashlib.sha512)
        sigdigest = base64.b64encode(signature.digest())

        return sigdigest.decode()
