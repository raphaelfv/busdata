from django.conf.urls import url
from django.contrib import admin
from busdata.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cadastro/$', inventario), #inventario de fotos
    url(r'^cadastro/empresa/$', cadastrarEmpresa),
]
