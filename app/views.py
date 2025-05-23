from django.shortcuts import render
from .models import Network, Networkmofa, Networkexxon, Networkemfa, Networkhorizon,Networkedsnew
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.translation import get_language






@login_required
@staff_member_required

def dashboard(request):
    data = {
        'EDS': Networkedsnew.objects.count(),
        'MOFA': Networkmofa.objects.count(),
        'EXXON': Networkexxon.objects.count(),
        'EMFA': Networkemfa.objects.count(),
        'HORIZON': Networkhorizon.objects.count(),
        'Main Network': Network.objects.count(),
    }
    return render(request, 'pages/dashboard.html', {'data': data})


# Create your views here.


def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')


def network(request):
    language = get_language()

    networks = Network.objects.all()

    # الفلاتر من الـ GET
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    # اختيار الأعمدة المناسبة حسب اللغة
    governorate_field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'
    speciality_field = 'speciality_ar' if language == 'ar' else 'speciality'

    # تطبيق الفلاتر
    if governorate:
        networks = networks.filter(**{governorate_field: governorate})
    if area:
        networks = networks.filter(**{area_field: area})
    if type:
        networks = networks.filter(**{type_field: type})
    if speciality:
        networks = networks.filter(**{speciality_field: speciality})

    if query:
        query_filter = Q(provider__icontains=query) | Q(address__icontains=query) | Q(phone__icontains=query) | Q(email__icontains=query) | Q(notes__icontains=query)
        if language == 'ar':
            query_filter |= Q(provider_ar__icontains=query) | Q(address_ar__icontains=query)
        networks = networks.filter(query_filter)

    # بيانات الفلاتر حسب اللغة
    governorates = Network.objects.values_list(governorate_field, flat=True).distinct()
    areas = Network.objects.values_list(area_field, flat=True).distinct()
    types = Network.objects.values_list(type_field, flat=True).distinct()
    specialities = Network.objects.values_list(speciality_field, flat=True).distinct()

    return render(request, 'pages/network.html', {
        'networks': networks,
        'governorates': sorted(filter(None, governorates)),
        'types': sorted(filter(None, types)),
        'specialities': sorted(filter(None, specialities)),
        'areas': sorted(filter(None, areas)),
        'language': language,  # مهم للتيمبلت
    })




def nav(request):
    return render(request,'parts/navbar.html')

def footer(request):
    return render(request,'parts/footer.html')


def get_areas(request):
    language = get_language()
    governorate = request.GET.get('governorate')

    field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'

    areas = Network.objects.filter(**{field: governorate}).values_list(area_field, flat=True).distinct()
    return JsonResponse({'areas': list(filter(None, areas))})

def get_types(request):
    language = get_language()
    area = request.GET.get('area')

    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'

    types = Network.objects.filter(**{area_field: area}).values_list(type_field, flat=True).distinct()
    return JsonResponse({'types': list(filter(None, types))})










# ========== MOFA ==========
def mofa(request):
    networks = Networkmofa.objects.all()
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    if governorate:
        networks = networks.filter(governorate=governorate)
    if area:
        networks = networks.filter(area=area)
    if type:
        networks = networks.filter(type=type)
    if speciality:
        networks = networks.filter(speciality=speciality)
    if query:
        networks = networks.filter(
            Q(provider__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(notes__icontains=query)
        )

    governorates = Networkmofa.objects.values_list('governorate', flat=True).distinct()
    areas = Networkmofa.objects.values_list('area', flat=True).distinct()
    types = Networkmofa.objects.values_list('type', flat=True).distinct()
    specialities = Networkmofa.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/mofa.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })

def get_areas_mofa(request):
    governorate = request.GET.get('governorate')
    areas = Networkmofa.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})

def get_types_mofa(request):
    area = request.GET.get('area')
    types = Networkmofa.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})


# ========== EXXON ==========
def exxon(request):
    networks = Networkexxon.objects.all()
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    if governorate:
        networks = networks.filter(governorate=governorate)
    if area:
        networks = networks.filter(area=area)
    if type:
        networks = networks.filter(type=type)
    if speciality:
        networks = networks.filter(speciality=speciality)
    if query:
        networks = networks.filter(
            Q(provider__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(notes__icontains=query)
        )

    governorates = Networkexxon.objects.values_list('governorate', flat=True).distinct()
    areas = Networkexxon.objects.values_list('area', flat=True).distinct()
    types = Networkexxon.objects.values_list('type', flat=True).distinct()
    specialities = Networkexxon.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/exxon.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })

def get_areas_exxon(request):
    governorate = request.GET.get('governorate')
    areas = Networkexxon.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})

def get_types_exxon(request):
    area = request.GET.get('area')
    types = Networkexxon.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})


# ========== EMFA ==========
def emfa(request):
    networks = Networkemfa.objects.all()
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    if governorate:
        networks = networks.filter(governorate=governorate)
    if area:
        networks = networks.filter(area=area)
    if type:
        networks = networks.filter(type=type)
    if speciality:
        networks = networks.filter(speciality=speciality)
    if query:
        networks = networks.filter(
            Q(provider__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(notes__icontains=query)
        )

    governorates = Networkemfa.objects.values_list('governorate', flat=True).distinct()
    areas = Networkemfa.objects.values_list('area', flat=True).distinct()
    types = Networkemfa.objects.values_list('type', flat=True).distinct()
    specialities = Networkemfa.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/emfa.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })

def get_areas_emfa(request):
    governorate = request.GET.get('governorate')
    areas = Networkemfa.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})

def get_types_emfa(request):
    area = request.GET.get('area')
    types = Networkemfa.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})


# ========== HORIZON ==========
def horizon(request):
    networks = Networkhorizon.objects.all()
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    if governorate:
        networks = networks.filter(governorate=governorate)
    if area:
        networks = networks.filter(area=area)
    if type:
        networks = networks.filter(type=type)
    if speciality:
        networks = networks.filter(speciality=speciality)
    if query:
        networks = networks.filter(
            Q(provider__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(notes__icontains=query)
        )

    governorates = Networkhorizon.objects.values_list('governorate', flat=True).distinct()
    areas = Networkhorizon.objects.values_list('area', flat=True).distinct()
    types = Networkhorizon.objects.values_list('type', flat=True).distinct()
    specialities = Networkhorizon.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/horizon.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })

def get_areas_horizon(request):
    governorate = request.GET.get('governorate')
    areas = Networkhorizon.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})

def get_types_horizon(request):
    area = request.GET.get('area')
    types = Networkhorizon.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})


# ========== EDS ==========
def eds(request):
    networks = Networkedsnew.objects.all()
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    if governorate:
        networks = networks.filter(governorate=governorate)
    if area:
        networks = networks.filter(area=area)
    if type:
        networks = networks.filter(type=type)
    if speciality:
        networks = networks.filter(speciality=speciality)
    if query:
        networks = networks.filter(
            Q(provider__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(notes__icontains=query)
        )

    governorates = Networkedsnew.objects.values_list('governorate', flat=True).distinct()
    areas = Networkedsnew.objects.values_list('area', flat=True).distinct()
    types = Networkedsnew.objects.values_list('type', flat=True).distinct()
    specialities = Networkedsnew.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/eds.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })

def get_areas_eds(request):
    governorate = request.GET.get('governorate')
    areas = Networkedsnew.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})

def get_types_eds(request):
    area = request.GET.get('area')
    types = Networkedsnew.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})