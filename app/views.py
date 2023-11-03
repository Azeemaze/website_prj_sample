from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'app/home.html')

def About(request):
    return render(request,'app/about.html')


def Service(request):
    return render(request,'app/service.html')


def Contact(request):
    return render(request,'app/contact.html')

def price(request):
    return render(request,'app/price.html')

def team(request):
    return render(request,'app/team.html')

def testimonial(request):
    return render(request,'app/testimonial.html')

def appointment(request):
    return render(request,'app/appointment.html')

