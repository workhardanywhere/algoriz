# -*- coding: utf-8 -*-
from django import forms
from tradebot.models import TradeCalc


class TradeCalcForm(forms.ModelForm):

    class Meta:
        model = TradeCalc
        fields = ('name', 'ticker', 'signal', 'trade')