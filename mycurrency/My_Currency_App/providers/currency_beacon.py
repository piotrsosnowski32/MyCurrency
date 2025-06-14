import requests
from django.conf import settings
from .base import BaseCurrencyProvider

class BeaconCurrencyProvider(BaseCurrencyProvider):
    name = "Currency"
    priority = 1
    
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
        
        return data["rates"][exchanged_currency]
          