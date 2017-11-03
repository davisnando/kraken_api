#!/usr/bin/python
import settings
from krakenuser import KrakenUser

API_KEY = settings.API_KEY
API_SECRET = settings.API_SECRET

if __name__ == "__main__":
    user = KrakenUser(API_KEY, API_SECRET)
    print(user.get_ratios())
