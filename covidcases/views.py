from django.shortcuts import render
from .models import Country,Patients

# Create your views here.

def home(request):
    all_countires = Country.objects.all()
    print(all_countires)
    context = {
        'all_countries': all_countires
    }

    return render(request, 'covidcases/home.html', context)