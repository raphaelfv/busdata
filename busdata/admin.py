# -*- coding: utf-8 -*-
from busdata.first_load import criarCarrocerias,criarConsorcios,criarEmpresas,criarFabricantes

from busdata.settings import DEBUG

if DEBUG:
    criarEmpresas()
    criarConsorcios()
    criarFabricantes()
    criarCarrocerias()
