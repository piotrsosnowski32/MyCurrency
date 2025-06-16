from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Currency, CurrencyExchangeRate
from .serializers import CurrencySerializer
from .providers.currency_beacon import BeaconCurrencyProvider
from .providers.mock import MockCurrencyProvider
from .services import get_exchange_rate_data, get_timeseries
from datetime import datetime as dt

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class ExchangeRateListView(APIView):
    def get(self, request):
        source = request.query_params.get('source')
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        symbols = request.query_params.get('symbols')
        rates = get_timeseries(source, date_from, date_to, symbols.split(","))
        
        return Response({source: rates})

class ConvertAmountView(APIView):
    def get(self, request):
        source_currency = request.query_params.get('source')
        exchanged_currency = request.query_params.get('exchanged')
        amount = float(request.query_params.get('amount'))
        
        rate = get_exchange_rate_data(source_currency, exchanged_currency, dt.today())
        
        if rate:
            return Response({"converted_amount": amount * float(rate), "rate": rate})
        
        return Response({"error": "Unable to get rate"}, status=status.HTTP_400_BAD_REQUEST)