from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from tradebot.views import home

urlpatterns = [
    re_path('^$', home, name='home'),
    path('admin/', admin.site.urls),
    path('tradebot/', include('tradebot.urls'))
]
