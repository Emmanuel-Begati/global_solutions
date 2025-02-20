from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')

def services(request):
    return render(request, 'website/services.html')

def pricing(request):
    return render(request, 'website/pricing.html')

def contact(request):
    return render(request, 'website/contact.html')

def team(request):
    return render(request, 'website/team.html')

def base(request):
    return render(request, 'website/base.html')