from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from .currency import CURRENCY

User = get_user_model()


class Portfolio(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='portfolios')
    currency = models.CharField(
        max_length=12, choices=CURRENCY, verbose_name="Криптовалюта"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'currency'],
                name='unique_user_currency'
            )
        ]

    def __str__(self):
        return "%s %s" % (self.user.username, self.currency)


class Buy(models.Model):
    def validate_interval(value):
        if value <= 0.0:
            raise ValidationError(
                ('%(value)s Покупка не может меньше или равна 0.'),
                params={'value': value},
            )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='buyes'
    )
    count = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[validate_interval])
    currency = models.CharField(
        max_length=12, choices=CURRENCY, verbose_name="Криптовалюта"
    )
    purchase_price = models.DecimalField(
        max_digits=20,
        decimal_places=5,
        verbose_name="Цена покупки",
        validators=[validate_interval]
    )
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=5,
        blank=True
    )

    def save(self, *args, **kwargs):
        self.amount = self.count * self.purchase_price
        print('self.amount', self.amount)
        super(Buy, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.count}'


class Sell(models.Model):
    def validate_interval(value):
        if value <= 0.0:
            raise ValidationError(
                ('%(value)s Продажа не может меньше или равна 0.'),
                params={'value': value},
            )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sells'
    )
    count = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        validators=[validate_interval])
    currency = models.CharField(
        max_length=12, choices=CURRENCY, verbose_name="Криптовалюта"
    )
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=5,
        blank=True
    )
    sale_price = models.DecimalField(
        max_digits=20,
        decimal_places=5,
        verbose_name="Цена продажи",
    )

    def save(self, *args, **kwargs):
        self.amount = self.count * self.sale_price
        print('self.amount', self.amount)
        super(Sell, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.count}'
