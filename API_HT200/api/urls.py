from django.urls import path
from .views import *


urlpatterns = [
     path('', homeView.as_view()),
     path('getTimeHT200', readTimeH200.as_view()),
     path('getFasesHT200', readFasesHT200.as_view()),
     path('getSecuenciaHT200', readSecuenciasHT200.as_view()),
]