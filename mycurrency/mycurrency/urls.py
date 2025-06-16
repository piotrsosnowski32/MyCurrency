from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from My_Currency_App.views import CurrencyViewSet, ExchangeRateListView, ConvertAmountView

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("api/exchange-rates/", ExchangeRateListView.as_view()),
    path("api/convert/", ConvertAmountView.as_view()),
]

