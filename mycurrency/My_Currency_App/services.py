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
            target_obj = Currency.objects.get(code=target)
            CurrencyExchangeRate.objects.create(
                source_currency=source_obj,
                exchanged_currency=target_obj,
                valuation_date=date,
                rate_value=rate_value
            )
            return rate_value
        except Exception as e:
            continue

    raise Exception("No provider succeeded.")