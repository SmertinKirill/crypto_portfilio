from django.contrib import admin

from .models import Buy, Portfolio, Sell

admin.site.register(Portfolio)
admin.site.register(Buy)
admin.site.register(Sell)
