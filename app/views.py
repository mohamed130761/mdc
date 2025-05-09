from django.shortcuts import render
from .models import Network
from django.db.models import Q
from django.http import JsonResponse

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
    networks = Network.objects.all()

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
    governorates = Network.objects.values_list('governorate', flat=True).distinct()
    areas = Network.objects.values_list('area', flat=True).distinct()
    types = Network.objects.values_list('type', flat=True).distinct()
    specialities = Network.objects.values_list('speciality', flat=True).distinct()

    return render(request, 'pages/network.html', {
        'networks': networks,
        'governorates': governorates,
        'types': types,
        'specialities': specialities,
        'areas': areas,
    })




def nav(request):
    return render(request,'parts/navbar.html')

def footer(request):
    return render(request,'parts/footer.html')


def get_areasen(request):
    governorate = request.GET.get('governorate')
    areas = Network.objects.filter(governorate=governorate).values_list('area', flat=True).distinct()
    return JsonResponse({'areas': list(areas)})

def get_typesen(request):
    area = request.GET.get('area')
    types = Network.objects.filter(area=area).values_list('type', flat=True).distinct()
    return JsonResponse({'types': list(types)})