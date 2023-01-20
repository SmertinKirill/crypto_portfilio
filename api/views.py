from rest_framework import mixins, viewsets

from api.serializers import (BuySerializers, PortfolioSerializers,
                             SellSerializers)
from portfolio.models import Buy, Portfolio, Sell


class PortfolioViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = PortfolioSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Portfolio.objects.filter(user_id=self.request.user)


class BuyViewSet(viewsets.ModelViewSet):
    serializer_class = BuySerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Buy.objects.filter(user_id=self.request.user)


class SellViewSet(viewsets.ModelViewSet):
    serializer_class = SellSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Sell.objects.filter(user_id=self.request.user)
