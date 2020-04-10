from django.contrib import admin
from trade import models  as trade_model
# Register your models here.
admin.site.register(trade_model.Order)