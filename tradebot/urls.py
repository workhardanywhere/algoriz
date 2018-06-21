from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from .views import TradeInputView, AlgoView, ShowGraphView

urlpatterns = [
    path('tradeinput/', TradeInputView.as_view(), name='tradeinput'),
    path('algoview/', AlgoView.as_view(), name='algo_view'),
    path('<int:pk>/plot/', ShowGraphView.as_view(), name='show_graph'),
]