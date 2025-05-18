from django.shortcuts import render
from .models import Networkar
from django.db.models import Q
from django.http import JsonResponse


# Create your views here.
def networkar(request):
    networks = Networkar.objects.all()

    # الفلاتر العادية
    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')  # البحث العام

    # تطبيق الفلاتر
    if governorate:
        networks = networks.filter(governorate=governorate)
    if area:
        networks = networks.filter(area=area)
    if type:
        networks = networks.filter(type=type)
    if speciality:
        networks = networks.filter(speciality=speciality)

    # تطبيق البحث العام
    if query:
        networks = networks.filter(
            Q(provider__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(notes__icontains=query)
        )

    # البيانات المستخدمة في الفلاتر
    governorates = Networkar.objects.values_list('governorate', flat=True).distinct()
    areas = Networkar.objects.values_list('area', flat=True).distinct()
    types = Networkar.objects.values_list('type', flat=True).distinct()
    specialities = Networkar.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/networkar.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })

def homear(request):
    return render(request,'pages/homear.html')

def aboutar(request):
    return render(request,'pages/aboutar.html')

def contactar(request):
    return render(request,'pages/contactar.html')

def navbarar(request):
    return render(request,'pages/navbarar.html')

def footerar(request):
    return render(request,'pages/footerar.html')


def get_areas(request):
    governorate = request.GET.get('governorate')
    areas = Networkar.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})

def get_types(request):
    area = request.GET.get('area')
    types = Networkar.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})


def edsar(request):
    return render(request,'pages/edsar.html')

def mofaar(request):
    return render(request,'pages/mofaar.html')

def exxonar(request):
    return render(request,'pages/exxonar.html')

def emfaar(request):
    return render(request,'pages/emfaar.html')

def horizonar(request):
    return render(request,'pages/horizonar.html')
