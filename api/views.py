from rest_framework import mixins, viewsets

from api.serializers import (BuySerializers, PortfolioSerializers,
                             SellSerializers)
from portfolio.models import Buy, Portfolio, Sell, Crypto
# from rest_framework import status
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PortfolioViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = PortfolioSerializers
    permission_class = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Portfolio.objects.filter(user_id=self.request.user)


class BuyViewSet(viewsets.ModelViewSet):
    serializer_class = BuySerializers
    permission_class = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Buy.objects.filter(user_id=self.request.user)


class SellViewSet(viewsets.ModelViewSet):
    serializer_class = SellSerializers
    permission_class = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Sell.objects.filter(user_id=self.request.user)
