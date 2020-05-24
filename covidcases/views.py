from django.shortcuts import render,get_object_or_404
from .models import Country,Patients

# Create your views here.

def home(request):
    all_countires = Country.objects.all()
    print(all_countires)
    context = {
        'all_countries': all_countires
    }

    return render(request, 'covidcases/home.html', context)

def details(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    all_patients = country.patients_set.all()
    context = {
        'all_patients': all_patients
    }

    return render(request, 'covidcases/details.html', context)

