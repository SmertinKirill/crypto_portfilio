# Generated by Django 3.2.16 on 2023-01-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='fffaff',
            field=models.DecimalField(blank=True, decimal_places=5, default=1, max_digits=20),
            preserve_default=False,
        ),
    ]
