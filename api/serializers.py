from rest_framework import serializers

from api.functions import get_price, get_profit, get_total
from portfolio.models import Buy, Portfolio, Sell, Crypto


class PortfolioSerializers(serializers.ModelSerializer):
    current_price = serializers.SerializerMethodField(read_only=True, )
    total = serializers.SerializerMethodField(read_only=True, default='0')
    profit = serializers.SerializerMethodField(read_only=True, default='0', )
    currency = serializers.SlugRelatedField(
        queryset=Crypto.objects.all(),
        slug_field='tag'
    )

    class Meta:
        model = Portfolio
        fields = ('currency', 'current_price', 'total', 'profit')

    def get_current_price(self, obj):
        current_price = get_price(str(obj.currency))
        return f'{current_price}$'

    def get_total(self, obj):
        return get_total(obj.user_id, obj.currency)

    def get_profit(self, obj):
        return get_profit(obj.user_id, obj.currency)


class BuySerializers(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    currency = serializers.SlugRelatedField(
        queryset=Crypto.objects.all(),
        slug_field='tag'
    )

    def create(self, validated_data):
        print(self.validated_data)
        buy = Buy.objects.create(**validated_data)
        return buy

    class Meta:
        model = Buy
        fields = '__all__'


class SellSerializers(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    currency = serializers.SlugRelatedField(
        queryset=Crypto.objects.all(),
        slug_field='tag'
    )

    class Meta:
        model = Sell
        fields = '__all__'
