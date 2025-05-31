from django.shortcuts import render
from .models import Network, Networkmofa, Networkexxon, Networkemfa, Networkhorizon,Networkedsnew
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.translation import get_language
from django.core.paginator import Paginator
from urllib.parse import urlencode
import uuid
from django.core.mail import EmailMessage
from .forms import PreAuthForm


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
    language=get_language()
    return render(request,'pages/contact.html',{'language':language})


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


    # Apply pagination
    paginator = Paginator(networks, 10)  # Show 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Smart pagination range
    current_page = page_obj.number
    total_pages = paginator.num_pages
    start_page = ((current_page - 1) // 10) * 10 + 1
    end_page = min(start_page + 9, total_pages)
    page_range = range(start_page, end_page + 1)

    # بيانات الفلاتر حسب اللغة
    governorates = Network.objects.values_list(governorate_field, flat=True).distinct()
    areas = Network.objects.values_list(area_field, flat=True).distinct()
    types = Network.objects.values_list(type_field, flat=True).distinct()
    specialities = Network.objects.values_list(speciality_field, flat=True).distinct()

    querydict = request.GET.copy()
    if 'page' in querydict:
        del querydict['page']
    query_string = urlencode(querydict)

    return render(request, 'pages/network.html', {
        'networks': page_obj,  # Pass paginated object
        'page_obj': page_obj,  # Also useful for pagination controls
        'page_range': page_range,  # <- this must be here
        'governorates': sorted(filter(None, governorates)),
        'types': sorted(filter(None, types)),
        'specialities': sorted(filter(None, specialities)),
        'areas': sorted(filter(None, areas)),
        'language': language,  # مهم للتيمبلت
        'query_string': query_string,

    })


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


def nav(request):
    language=get_language()
    return render(request,'parts/navbar.html',{'language':language})

def footer(request):
    return render(request,'parts/footer.html')













# ========== MOFA ==========
def mofa(request):
    language = get_language()
    networks = Networkmofa.objects.all()

    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    governorate_field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'
    speciality_field = 'speciality_ar' if language == 'ar' else 'speciality'

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

    paginator = Paginator(networks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_page = page_obj.number
    total_pages = paginator.num_pages
    start_page = ((current_page - 1) // 10) * 10 + 1
    end_page = min(start_page + 9, total_pages)
    page_range = range(start_page, end_page + 1)

    governorates = Networkmofa.objects.values_list(governorate_field, flat=True).distinct()
    areas = Networkmofa.objects.values_list(area_field, flat=True).distinct()
    types = Networkmofa.objects.values_list(type_field, flat=True).distinct()
    specialities = Networkmofa.objects.values_list(speciality_field, flat=True).distinct()

    querydict = request.GET.copy()
    if 'page' in querydict:
        del querydict['page']
    query_string = urlencode(querydict)

    return render(request, 'pages/mofa.html', {
        'networks': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'governorates': sorted(filter(None, governorates)),
        'types': sorted(filter(None, types)),
        'specialities': sorted(filter(None, specialities)),
        'areas': sorted(filter(None, areas)),
        'language': language,
        'query_string': query_string,
    })

def get_areas_mofa(request):
    language = get_language()
    governorate = request.GET.get('governorate')
    field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'
    areas = Networkmofa.objects.filter(**{field: governorate}).values_list(area_field, flat=True).distinct()
    return JsonResponse({'areas': list(filter(None, areas))})

def get_types_mofa(request):
    language = get_language()
    area = request.GET.get('area')
    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'
    types = Networkmofa.objects.filter(**{area_field: area}).values_list(type_field, flat=True).distinct()
    return JsonResponse({'types': list(filter(None, types))})




# ========== EXXON ==========
def exxon(request):
    language = get_language()
    networks = Networkexxon.objects.all()

    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    governorate_field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'
    speciality_field = 'speciality_ar' if language == 'ar' else 'speciality'

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

    paginator = Paginator(networks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_page = page_obj.number
    total_pages = paginator.num_pages
    start_page = ((current_page - 1) // 10) * 10 + 1
    end_page = min(start_page + 9, total_pages)
    page_range = range(start_page, end_page + 1)

    governorates = Networkexxon.objects.values_list(governorate_field, flat=True).distinct()
    areas = Networkexxon.objects.values_list(area_field, flat=True).distinct()
    types = Networkexxon.objects.values_list(type_field, flat=True).distinct()
    specialities = Networkexxon.objects.values_list(speciality_field, flat=True).distinct()

    querydict = request.GET.copy()
    if 'page' in querydict:
        del querydict['page']
    query_string = urlencode(querydict)

    return render(request, 'pages/exxon.html', {
        'networks': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'governorates': sorted(filter(None, governorates)),
        'types': sorted(filter(None, types)),
        'specialities': sorted(filter(None, specialities)),
        'areas': sorted(filter(None, areas)),
        'language': language,
        'query_string': query_string,
    })

def get_areas_exxon(request):
    language = get_language()
    governorate = request.GET.get('governorate')
    field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'
    areas = Networkexxon.objects.filter(**{field: governorate}).values_list(area_field, flat=True).distinct()
    return JsonResponse({'areas': list(filter(None, areas))})

def get_types_exxon(request):
    language = get_language()
    area = request.GET.get('area')
    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'
    types = Networkexxon.objects.filter(**{area_field: area}).values_list(type_field, flat=True).distinct()
    return JsonResponse({'types': list(filter(None, types))})




# ========== EMFA ==========
def emfa(request):
    language = get_language()
    networks = Networkemfa.objects.all()

    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    governorate_field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'
    speciality_field = 'speciality_ar' if language == 'ar' else 'speciality'

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

    paginator = Paginator(networks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_page = page_obj.number
    total_pages = paginator.num_pages
    start_page = ((current_page - 1) // 10) * 10 + 1
    end_page = min(start_page + 9, total_pages)
    page_range = range(start_page, end_page + 1)

    governorates = Networkemfa.objects.values_list(governorate_field, flat=True).distinct()
    areas = Networkemfa.objects.values_list(area_field, flat=True).distinct()
    types = Networkemfa.objects.values_list(type_field, flat=True).distinct()
    specialities = Networkemfa.objects.values_list(speciality_field, flat=True).distinct()

    querydict = request.GET.copy()
    if 'page' in querydict:
        del querydict['page']
    query_string = urlencode(querydict)

    return render(request, 'pages/emfa.html', {
        'networks': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'governorates': sorted(filter(None, governorates)),
        'types': sorted(filter(None, types)),
        'specialities': sorted(filter(None, specialities)),
        'areas': sorted(filter(None, areas)),
        'language': language,
        'query_string': query_string,
    })

def get_areas_emfa(request):
    language = get_language()
    governorate = request.GET.get('governorate')
    field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'
    areas = Networkemfa.objects.filter(**{field: governorate}).values_list(area_field, flat=True).distinct()
    return JsonResponse({'areas': list(filter(None, areas))})

def get_types_emfa(request):
    language = get_language()
    area = request.GET.get('area')
    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'
    types = Networkemfa.objects.filter(**{area_field: area}).values_list(type_field, flat=True).distinct()
    return JsonResponse({'types': list(filter(None, types))})




# ========== HORIZON ==========
def horizon(request):
    language = get_language()
    networks = Networkhorizon.objects.all()

    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    governorate_field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'
    speciality_field = 'speciality_ar' if language == 'ar' else 'speciality'

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

    paginator = Paginator(networks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_page = page_obj.number
    total_pages = paginator.num_pages
    start_page = ((current_page - 1) // 10) * 10 + 1
    end_page = min(start_page + 9, total_pages)
    page_range = range(start_page, end_page + 1)

    governorates = Networkhorizon.objects.values_list(governorate_field, flat=True).distinct()
    areas = Networkhorizon.objects.values_list(area_field, flat=True).distinct()
    types = Networkhorizon.objects.values_list(type_field, flat=True).distinct()
    specialities = Networkhorizon.objects.values_list(speciality_field, flat=True).distinct()

    querydict = request.GET.copy()
    if 'page' in querydict:
        del querydict['page']
    query_string = urlencode(querydict)

    return render(request, 'pages/horizon.html', {
        'networks': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'governorates': sorted(filter(None, governorates)),
        'types': sorted(filter(None, types)),
        'specialities': sorted(filter(None, specialities)),
        'areas': sorted(filter(None, areas)),
        'language': language,
        'query_string': query_string,
    })

def get_areas_horizon(request):
    language = get_language()
    governorate = request.GET.get('governorate')
    field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'
    areas = Networkhorizon.objects.filter(**{field: governorate}).values_list(area_field, flat=True).distinct()
    return JsonResponse({'areas': list(filter(None, areas))})

def get_types_horizon(request):
    language = get_language()
    area = request.GET.get('area')
    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'
    types = Networkhorizon.objects.filter(**{area_field: area}).values_list(type_field, flat=True).distinct()
    return JsonResponse({'types': list(filter(None, types))})




# ========== EDS ==========


def eds(request):
    language = get_language()
    networks = Networkedsnew.objects.all()

    governorate = request.GET.get('governorate')
    area = request.GET.get('area')
    type = request.GET.get('type')
    speciality = request.GET.get('speciality')
    query = request.GET.get('query')

    governorate_field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'
    speciality_field = 'speciality_ar' if language == 'ar' else 'speciality'

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

    paginator = Paginator(networks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_page = page_obj.number
    total_pages = paginator.num_pages
    start_page = ((current_page - 1) // 10) * 10 + 1
    end_page = min(start_page + 9, total_pages)
    page_range = range(start_page, end_page + 1)

    governorates = Networkedsnew.objects.values_list(governorate_field, flat=True).distinct()
    areas = Networkedsnew.objects.values_list(area_field, flat=True).distinct()
    types = Networkedsnew.objects.values_list(type_field, flat=True).distinct()
    specialities = Networkedsnew.objects.values_list(speciality_field, flat=True).distinct()

    querydict = request.GET.copy()
    if 'page' in querydict:
        del querydict['page']
    query_string = urlencode(querydict)

    return render(request, 'pages/eds.html', {
        'networks': page_obj,
        'page_obj': page_obj,
        'page_range': page_range,
        'governorates': sorted(filter(None, governorates)),
        'types': sorted(filter(None, types)),
        'specialities': sorted(filter(None, specialities)),
        'areas': sorted(filter(None, areas)),
        'language': language,
        'query_string': query_string,
    })

def get_areas_eds(request):
    language = get_language()
    governorate = request.GET.get('governorate')
    field = 'governorate_ar' if language == 'ar' else 'governorate'
    area_field = 'area_ar' if language == 'ar' else 'area'
    areas = Networkedsnew.objects.filter(**{field: governorate}).values_list(area_field, flat=True).distinct()
    return JsonResponse({'areas': list(filter(None, areas))})

def get_types_eds(request):
    language = get_language()
    area = request.GET.get('area')
    area_field = 'area_ar' if language == 'ar' else 'area'
    type_field = 'type_ar' if language == 'ar' else 'type'
    types = Networkedsnew.objects.filter(**{area_field: area}).values_list(type_field, flat=True).distinct()
    return JsonResponse({'types': list(filter(None, types))})

#--------------------pre-auth ----------------------------

def preauth_view(request):
    reference_number = None

    if request.method == 'POST':
        form = PreAuthForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            reference_number = str(uuid.uuid4()).split('-')[0]  # توليد رقم مرجعي مختصر

            subject = f"طلب موافقة جديد - رقم مرجعي: {reference_number}"
            body = f"""
            الاسم: {cd['name']}
            التواصل: {cd['contact']}
            نوع الخدمة: {cd['service_type']}
            وصف: {cd['description']}
            الرقم المرجعي: {reference_number}
            """

            email = EmailMessage(
                subject,
                body,
                to=['mohamed130761@gmail.com'],  # عدل البريد هنا
            )

            if request.FILES.get('file'):
                email.attach(request.FILES['file'].name, request.FILES['file'].read(), request.FILES['file'].content_type)

            email.send()

            return render(request, 'pages/preauth.html', {
                'form': PreAuthForm(),
                'reference': reference_number,
                'success': True
            })

    else:
        form = PreAuthForm()

    return render(request, 'pages/preauth.html', {'form': form})
