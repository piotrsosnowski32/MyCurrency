from abc import ABC, abstractmethod

class BaseCurrencyProvider(ABC):
    name = None
    priority = 1
    is_active = True
        
    @abstractmethod
    def get_rate(self, source_currency, exchanged_currency, date):
        pass
    