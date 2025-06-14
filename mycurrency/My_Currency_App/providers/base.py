from abc import ABC, abstractmethod

class BaseCurrencyProvider(ABC):
    name = None
    priority = 1
        
    @abstractmethod
    def get_rate(self, source_currency, exchanged_currency, date):
        pass
    