# Generated by Django 3.2.16 on 2023-03-02 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20230302_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='buyes', to='portfolio.crypto'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sells', to='portfolio.crypto'),
        ),
    ]
