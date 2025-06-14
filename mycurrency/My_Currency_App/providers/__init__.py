from .currency_beacon import BeaconCurrencyProvider

ALL_PROVIDERS = [
    BeaconCurrencyProvider()
]

def get_active_providers():
    return sorted(ALL_PROVIDERS, key=lambda p: p.priority)