from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('medical_network/',views.network,name='network'),
    path('get-areasen/', views.get_areasen, name='get_areasen'),
    path('get-typesen/', views.get_typesen, name='get_typesen'),
    path('eds/',views.eds,name='eds'),
    path('mofa/',views.mofa,name='mofa'),
    path('exxon/',views.exxon,name='exxon'),
    path('emfa/',views.emfa,name='emfa'),
    path('horizon/',views.horizon,name='horizon'),

]