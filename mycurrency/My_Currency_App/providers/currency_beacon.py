import requests
from django.conf import settings
from .base import BaseCurrencyProvider

class BeaconCurrencyProvider(BaseCurrencyProvider):
    name = "Currency"
    priority = 1
    is_active=False
    
    def get_rate(self, source_currency, exchanged_currency, date):

        url = f"https://api.currencybeacon.com/v1/historical"
        params = {
            "api_key" : settings.CURRENCY_BEACON_API_KEY,
            "base" : source_currency,
            "symbols" : exchanged_currency,
            "date" : date
        }

        res = requests.get(url, params=params)

        if res.status_code != 200:
            raise Exception("CurrencyBeacon API failed")

        data = res.json()

        if not data["rates"]:
            raise Exception("Beacon has no rates")
 
        return data["rates"][exchanged_currency]
          
    def get_timeseries(self, source_currency, start_date, end_date, symbols):
        url = f"https://api.currencybeacon.com/v1/timeseries"
        params = {
            "api_key" : settings.CURRENCY_BEACON_API_KEY,
            "base" : source_currency,
            "symbols" : symbols,
            "start_date" : start_date,
            "end_date": end_date
        }
          
        res = requests.get(url, params=params)

        if res.status_code != 200:
            raise Exception("CurrencyBeacon API failed")

        data = res.json()
        print(data)