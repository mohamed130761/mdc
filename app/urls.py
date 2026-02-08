from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [

    # ===== Core Pages =====
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # ===== Main Medical Networks =====
    path('discount/', views.network, name='network'),
    path('eds/', views.eds, name='eds'),
    path('mofa/', views.mofa, name='mofa'),
    path('exxon/', views.exxon, name='exxon'),
    path('emfa/', views.emfa, name='emfa'),
    path('horizon/', views.horizon, name='horizon'),

    # 🆕 Horizon Global Network
    path('horizon-global/', views.horizon_global_network, name='horizon_global_network'),

    # ===== PreAuth =====
    path('preauth/', views.preauth_view, name='preauth'),

    # ===== Generic Network AJAX =====
    path('get-areas/', views.get_areas, name='get_areas'),
    path('get-types/', views.get_types, name='get_types'),

    # ===== AJAX – MOFA =====
    path('ajax/mofa/areas/', views.get_areas_mofa, name='get_areas_mofa'),
    path('ajax/mofa/types/', views.get_types_mofa, name='get_types_mofa'),

    # ===== AJAX – EXXON =====
    path('ajax/exxon/areas/', views.get_areas_exxon, name='get_areas_exxon'),
    path('ajax/exxon/types/', views.get_types_exxon, name='get_types_exxon'),

    # ===== AJAX – EMFA =====
    path('ajax/emfa/areas/', views.get_areas_emfa, name='get_areas_emfa'),
    path('ajax/emfa/types/', views.get_types_emfa, name='get_types_emfa'),

    # ===== AJAX – HORIZON =====
    path('ajax/horizon/areas/', views.get_areas_horizon, name='get_areas_horizon'),
    path('ajax/horizon/types/', views.get_types_horizon, name='get_types_horizon'),

    # 🆕 ===== AJAX – HORIZON GLOBAL =====
    path('ajax/horizon-global/areas/', views.get_areas_horizon_global, name='get_areas_horizon_global'),
    path('ajax/horizon-global/types/', views.get_types_horizon_global, name='get_types_horizon_global'),

    # ===== AJAX – EDS =====
    path('ajax/eds/areas/', views.get_areas_eds, name='get_areas_eds'),
    path('ajax/eds/types/', views.get_types_eds, name='get_types_eds'),

]
