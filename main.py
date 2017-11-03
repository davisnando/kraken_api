#!/usr/bin/python
import settings
from krakenuser import KrakenUser
from krakenapi import Krakenapi
API_KEY = settings.API_KEY
API_SECRET = settings.API_SECRET

if __name__ == "__main__":
    api = Krakenapi(API_KEY, API_SECRET)
    user = KrakenUser(api)
    print(user.get_ratios())
