import random
from django.conf import settings
from .base import BaseCurrencyProvider

class MockCurrencyProvider(BaseCurrencyProvider):
    name = "Currency"
    priority = 2
    is_active = True
    
    def get_rate(self, source_currency, exchanged_currency, date):
        return round(random.uniform(0.5, 2.0), 6)
    
    def get_timeseries(self, source, start_date, end_date, symbol):
        if source == symbol:
            return 1
        return round(random.uniform(0.5, 2.0), 6)
    
    