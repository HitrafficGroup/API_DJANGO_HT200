from django.urls import path
from .views import *


urlpatterns = [
     path('', homeView.as_view()),
     #funciones de lectura HT200
     path('getTimeHT200', readTimeH200.as_view()),
     path('getFasesHT200', readFasesHT200.as_view()),
     path('getSecuenciaHT200', readSecuenciasHT200.as_view()),
     path('getSplitHT200', readSplitHT200.as_view()),
     path('getPatternHT200', readPatternHT200.as_view()),
     path('getAccionHT200', readAccionHT200.as_view()),
     path('getPlanesHT200', readPlanesHT200.as_view()),
     path('getScneduleHT200', readScneduleHT200.as_view()),
     path('getDeviceInfoHT200', readDeviceInfoHT200.as_view()),
     path('getBasicInfoHT200', readBasicInfoHT200.as_view()),
     path('getUnitHT200', readUnitHT200.as_view()),
     path('getChannelHT200', readChannelHT200.as_view()),
     path('getCoordlHT200', readCoordHT200.as_view()),
     path('getOverlapHT200', readOverlapHT200.as_view()),
     #funciones de escritura HT200
     path('setUnitHT200',setUnitHT200.as_view()),
     path('setFasesHT200',setFasesHT200.as_view()),
     path('setSecuenciasHT200',setSecuenciasHT200.as_view()),
     path('setSplitHT200',setSplitHT200.as_view()),
     path('setPatternHT200',setPatternHT200.as_view()),
     path('setActionHT200',setActionHT200.as_view()),
     path('setPlanHT200',setPlanHT200.as_view()),
     path('setHorariosHT200',setHorariosHT200.as_view()),
     path('setChannelHT200',setChannelHT200.as_view()),
     path('setIpTarget',setIpTarget.as_view()),
     #funciones de lectura sw12
     path('getFasesSW12', getFasesSW12.as_view()),
     path('getOrdinaryScheduleSW12', getOrdinaryScheduleSW12.as_view()),
]