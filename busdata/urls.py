from django.conf.urls import url
from django.contrib import admin
from busdata.views import *

urlpatterns = [
    url(r'^$', inventario),
    url(r'^admin/', admin.site.urls),
    url(r'^cadastro/registro$', cadastrarFoto),
    url(r'^cadastro/registro/(?P<registroID>\d+)$', cadastrarFoto),
]
