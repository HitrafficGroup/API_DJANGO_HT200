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
     path('setTimeHT200',setTimeHT200.as_view()),
     path('setIpTarget',setIpTarget.as_view()),
     path('setBasicPlan',setBasicPlan.as_view()),
     #funciones de lectura sw12
     path('getFasesSW12', getFasesSW12.as_view()),
     path('getOrdinaryScheduleSW12', getOrdinaryScheduleSW12.as_view()),
     path('getWeekendScheduleSW12', getWeekendScheduleSW12.as_view()),
     path('getFestivalScheduleSW12', getFestivalScheduleSW12.as_view()),
     path('getGruposSW12', getGruposSW12.as_view()),
     path('getGreenConflictSW12', getGreenConflictSW12.as_view()),
     path('getOperativeParamsSW12', getOperativeParamsSW12.as_view()),
     path('getPlan1SW12', getPlan1SW12.as_view()),
     path('getPlan2SW12', getPlan2SW12.as_view()),
     path('getPlan3SW12', getPlan3SW12.as_view()),
     path('getPlan4SW12', getPlan4SW12.as_view()),
     path('getPlan5SW12', getPlan5SW12.as_view()),
     path('getPlan6SW12', getPlan6SW12.as_view()),
     path('getPlan7SW12', getPlan7SW12.as_view()),
     path('getPlan8SW12', getPlan8SW12.as_view()),
     path('getTimeControllerSW12', getTimeControllerSW12.as_view()),
     path('getSpecialDaysSW12', getSpecialDaysSW12.as_view()),
     path('getEntradasSW12', getEntradasSW12.as_view()),
     path('getErroresSW12', getErroresSW12.as_view()),
     #funciones de escritura sw12
     path('postFasesSW12',postFasesSW12.as_view()),
     path('postGruposSW12',postGruposSW12.as_view()),
     path('postGreenConflictSW12',postGreenConflictSW12.as_view()),
     path('postPlanesSW12',postPlanesSW12.as_view()),
     path('postOtrosParametrosSW12',postOtrosParametrosSW12.as_view()),
     path('postHorariosSW12',postHorariosSW12.as_view()),
     path('postDiasEspecialesSW12',postDiasEspecialesSW12.as_view()),
     path('postEntradasSW12',postEntradasSW12.as_view()),
     path('postTimeSW12',postTimeSW12.as_view()),
]