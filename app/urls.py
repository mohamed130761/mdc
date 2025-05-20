from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('dashboard/', views.dashboard, name='dashboard'),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('medical_network/',views.network,name='network'),
    path('get-areasen/', views.get_areasen, name='get_areasen'),
    path('get-typesen/', views.get_typesen, name='get_typesen'),
    path('eds/', views.eds, name='eds'),
    path('mofa/', views.mofa, name='mofa'),
    path('exxon/', views.exxon, name='exxon'),
    path('emfa/', views.emfa, name='emfa'),
    path('horizon/', views.horizon, name='horizon'),



    # AJAX endpoints for MOFA
    path('ajax/mofa/areas/', views.get_areas_mofa, name='get_areas_mofa'),
    path('ajax/mofa/types/', views.get_types_mofa, name='get_types_mofa'),

    # AJAX endpoints for EXXON
    path('ajax/exxon/areas/', views.get_areas_exxon, name='get_areas_exxon'),
    path('ajax/exxon/types/', views.get_types_exxon, name='get_types_exxon'),

    # AJAX endpoints for EMFA
    path('ajax/emfa/areas/', views.get_areas_emfa, name='get_areas_emfa'),
    path('ajax/emfa/types/', views.get_types_emfa, name='get_types_emfa'),

    # AJAX endpoints for HORIZON
    path('ajax/horizon/areas/', views.get_areas_horizon, name='get_areas_horizon'),
    path('ajax/horizon/types/', views.get_types_horizon, name='get_types_horizon'),

    # AJAX endpoints for EDS
    path('ajax/eds/areas/', views.get_areas_eds, name='get_areas_eds'),
    path('ajax/eds/types/', views.get_types_eds, name='get_types_eds'),


]