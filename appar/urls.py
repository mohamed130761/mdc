from django.urls import path
from . import views

urlpatterns=[
    path('',views.homear,name='homear'),
    path('aboutar',views.aboutar,name='aboutar'),
    path('contactar',views.contactar,name='contactar'),
    path('medical_networkar/',views.networkar, name='networkar'),
]