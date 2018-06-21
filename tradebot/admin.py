from django.contrib import admin
from .models import TradeCalc


@admin.register(TradeCalc)
class TradeCalcAdmin(admin.ModelAdmin):
    pass