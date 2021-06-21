from django.urls import path
from .views import index, curriculo_marcos,curriculo_victor, lista

urlpatterns = [
    path('', index, name='index'),
    path('curriculo_marcos/', curriculo_marcos, name='marcos'),
    path('curriculo_victor/', curriculo_victor, name='victor'),
    path('lista/', lista, name='lista'),
]