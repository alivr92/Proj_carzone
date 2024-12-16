from django.shortcuts import render
from .models import Team
from app_cars.models import Car


# Create your views here.


def home(request):
    team_members = Team.objects.all()
    featured_cars = Car.objects.all().order_by('created_date').filter(is_featured=True)
    all_cars = Car.objects.all().order_by('-created_date')
    context = {
        'team_members': team_members,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'app_pages/index.html', context)


def about(request):
    team_members = Team.objects.all()
    context = {'team_members': team_members}
    return render(request, 'app_pages/about.html', context)


def services(request):
    context ={}
    return render(request, 'app_pages/services.html', context)


def contact(request):
    context = {}
    return render(request, 'app_pages/contact.html', context)
