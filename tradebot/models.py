import datetime
import numpy
from django.db import models
from .utils import pulldata
from .helper import algo_result

# Create your models here.
class TradeCalc(models.Model):
    name = models.CharField('Algo name', max_length=1024)
    signal = models.CharField('Signal', max_length=1024)
    trade = models.CharField('Trade', max_length=1024)
    ticker = models.CharField('Ticker', max_length=1024)

    @property
    def average_PnL(self):
        dump = pulldata(self.ticker)

        # sort by date
        sorted_dump = sorted(dump, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d'))

        try:
            positions, PnL = algo_result(
                    self.signal,
                    self.trade,
                    [x['close'] for x in sorted_dump]
            )
        except:
            return 0

        return numpy.average(PnL)

    class Meta:
        verbose_name = 'Trade algorithm'
        verbose_name_plural = 'Trade algorithms'
