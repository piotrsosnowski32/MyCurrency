from .models import Currency, CurrencyExchangeRate
from .providers import get_active_providers

def get_exchange_rate_data(source: str, target: str, date: str):

    rate = CurrencyExchangeRate.objects.filter(
        source_currency__code=source,
        exchanged_currency__code=target,
        valuation_date=date
    ).first()

    if rate:
        return rate.rate_value

    for provider in get_active_providers():
        try:
            rate_value = provider.get_rate(source, target, date)
            source_obj = Currency.objects.get(code=source)
            exchanged_obj = Currency.objects.get(code=target)
            
            CurrencyExchangeRate.objects.create(
                source_currency=source_obj,
                exchanged_currency=exchanged_obj,
                valuation_date=date,
                rate_value=rate_value
            )
        
            return rate_value
        except Exception as e:
            continue

    raise Exception("No provider succeeded.")

def get_timeseries(source: str, start_date: str, end_date: str, symbols: list):
    result = {}
    for exchange_sym in symbols:
        rate = CurrencyExchangeRate.objects.filter(
            source_currency__code=source,
            exchanged_currency__code=exchange_sym,
            valuation_date__range=[start_date, end_date]
        ).first()

        if rate:
            result[exchange_sym] = rate.rate_value

        for provider in get_active_providers():
            try:
                rate_value = provider.get_timeseries(source, start_date, end_date, exchange_sym)
                result[exchange_sym] = rate_value
            except Exception as e:
                continue
    
    if not result:
        raise Exception("No provider succeeded.")
    
    return result

    


    