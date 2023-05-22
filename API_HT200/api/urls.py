from django.urls import path
from .views import *


urlpatterns = [
     path('', homeView.as_view()),
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
     #funciones de escritura
     path('setUnitHT200',setUnitHT200.as_view()),
     path('setFasesHT200',setFasesHT200.as_view()),
     path('setSecuenciasHT200',setSecuenciasHT200.as_view()),
]