from django.shortcuts import render, redirect
from .models import Hero, Section, WhyUsSection, WhyUsFeature, Feature,ContactInfo,SocialLink, UsefulLink, Service, AboutTitle, AboutUs
from .models import Testimonial,Skill,SkillCategory,SkillFeature
from  django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# from .models import Notification, Message, Profile
# Create your views here.

@login_required(login_url='Learn:login')
def index(request):
    hero = Hero.objects.all()
    section = Section.objects.all()
    why = WhyUsSection.objects.first()
    why_feature = WhyUsFeature.objects.all()
    feature = Feature.objects.all()
    info = ContactInfo.objects.all()
    link = SocialLink.objects.all()
    use = UsefulLink.objects.all()
    service = Service.objects.all()

    context = {
        'hero':hero,
        'section':section,
        'why':why,
        'why_feature':why_feature,
        'feature':feature,
        'info':info,
        'link':link,
        'use':use,
        'service':service
    }
    return render(request,'index.html',context)

@login_required(login_url='Learn:login')
def about(request):
    about = AboutTitle.objects.all()
    aboutus = AboutUs.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        'about':about,
        'aboutus':aboutus,
        'testimonial':testimonial
    }
    return render(request,'about.html', context)

@login_required(login_url='Learn:login')
def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='Learn:login')
def skills(request):

    return render(request,'skills.html')


@login_required(login_url='Learn:login')
def layout(request):
    return render(request,'layout.html')




def registerPage(request):
    if request.user.is_authenticated:
        return redirect('Learn:dashboard')
    else:

        form = CreateUserForm()
    

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save() 
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)

                return redirect('Learn:login')

        context = {'form':form}
        return render (request,'register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Learn:dashboard')
    else:


        if request.method == 'POST':
            username =request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Learn:dashboard')
            
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render (request, 'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('Learn:login')


def layout1(request):
    return render(request,'layout1.html')

def dashboard(request):
    return render(request,'dashboard.html')


def explore_skills(request):
    skillctgry = SkillCategory.objects.all()
    feature = SkillFeature.objects.all()
    context = {
        'skillctgry':skillctgry,
        'feature':feature
    }
    return render(request,'explore_skills.html',context)

def my_skills(request):
    return render(request,'my_skills.html')

def upload_skill(request):
    return render(request,'upload_skills.html')

def requests(request):
    return render(request,'requests.html')

def analytics(request):
    return render(request,'analytics.html')


def newsletters(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        return JsonResponse({'message': 'Subscription successful'})













































































