# Generated by Django 3.2.16 on 2023-01-09 19:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import portfolio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=2, max_digits=20, validators=[portfolio.models.Sell.validate_interval])),
                ('currency', models.CharField(choices=[('BTC', 'Bitcoin'), ('ETH', 'Ethereum'), ('USDT', 'Tether')], max_length=8, verbose_name='Криптовалюта')),
                ('amount', models.DecimalField(blank=True, decimal_places=5, max_digits=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sells', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('BTC', 'Bitcoin'), ('ETH', 'Ethereum'), ('USDT', 'Tether')], max_length=8, verbose_name='Криптовалюта')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=2, max_digits=20, validators=[portfolio.models.Buy.validate_interval])),
                ('currency', models.CharField(choices=[('BTC', 'Bitcoin'), ('ETH', 'Ethereum'), ('USDT', 'Tether')], max_length=8, verbose_name='Криптовалюта')),
                ('purchase_price', models.DecimalField(decimal_places=5, max_digits=20, validators=[portfolio.models.Buy.validate_interval], verbose_name='Цена покупки')),
                ('amount', models.DecimalField(blank=True, decimal_places=5, max_digits=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
