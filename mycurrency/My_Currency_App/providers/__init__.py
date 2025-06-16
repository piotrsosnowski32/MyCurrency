from .currency_beacon import BeaconCurrencyProvider
from .mock import MockCurrencyProvider

ALL_PROVIDERS = [
    BeaconCurrencyProvider(),
    MockCurrencyProvider()
]

def get_active_providers():
    return sorted([p for p in ALL_PROVIDERS if p.is_active], key=lambda p: p.priority)