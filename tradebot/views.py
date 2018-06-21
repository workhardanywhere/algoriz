import operator
import datetime
import numpy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
import matplotlib
matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# import io
# import base64
# import PIL.Image

from .forms import TradeCalcForm
from .models import TradeCalc
from .helper import algo_result
from.utils import pulldata


def home(request):
    return redirect('/tradebot/tradeinput/')


class AlgoView(TemplateView):
    template_name = 'algo_view.html'

    def get_context_data(self, **kwargs):
        context = super(AlgoView, self).get_context_data(**kwargs)
        algorithms = TradeCalc.objects.all()
        context['algorithms'] = algorithms
        return context


class TradeInputView(FormView):
    template_name = 'trade_input.html'
    form_class = TradeCalcForm
    success_url = '/tradebot/algoview/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ShowGraphView(TemplateView):
    template_name = 'show_graph.html'

    def get_context_data(self, **kwargs):
        context = super(ShowGraphView, self).get_context_data(**kwargs)

        pk = kwargs.get('pk', None)

        plot_data = TradeCalc.objects.get(pk=pk)

        dump = pulldata(plot_data.ticker)

        # sort by date
        sorted_dump = sorted(dump, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d'))

        positions, PnL = algo_result(
                plot_data.signal,
                plot_data.trade,
                [x['close'] for x in sorted_dump]
        )

        context['positions'] = positions

        # fig = plt.figure()
        # plt.plot(numpy.arange(len(positions)), positions)
        # canvas = fig.canvas
        # buf, size = canvas.print_to_buffer()
        # image = PIL.Image.frombuffer('RGBA', size, buf, 'raw', 'RGBA', 0, 1)
        # buffer=io.BytesIO()
        #
        # image.save(buffer,'PNG')
        #
        # context['graphic'] = base64.b64encode(buffer.getvalue()).decode()
        # buffer.close()


        return context