from django.urls import path
from . import views

urlpatterns=[
    path('',views.homear,name='homear'),
    path('aboutar',views.aboutar,name='aboutar'),
    path('contactar',views.contactar,name='contactar'),
    path('medical_networkar/',views.networkar, name='networkar'),
    path('get-areas/', views.get_areas, name='get_areas'),
    path('get-types/', views.get_types, name='get_types'),
    path('edsar/',views.edsar,name='edsar'),
    path('mofaar/',views.mofaar,name='mofaar'),
    path('exxonar/',views.exxonar,name='exxonar'),
    path('emfaar/',views.emfaar,name='emfaar'),
    path('horizonar/',views.horizonar,name='horizonar'),
]