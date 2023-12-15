from django.http import HttpRequest,HttpResponse
from django.shortcuts import render ,redirect
from django.contrib import messages  # Import messages for displaying messages to the user
from .models import EventOrganizer
from django.db import models
from .models import UserRegistration


def registerlink(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        gender = request.POST['gender']
        enrollment = request.POST['enrollment']
        password = request.POST['password']

        # Create and save the user registration object
        user_registration = UserRegistration(
            fullname=fullname,
            username=username,
            email=email,
            gender=gender,
            enrollment=enrollment,
            password=password,
        )
        user_registration.save()

        # Redirect to a success page or homepage
        return redirect('logins')  
    return render(request,'register.html',{})

def home(request):
     
    return render(request,"home.html",{})



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Try to get the user by email
            user = UserRegistration.objects.get(email=email)
        except UserRegistration.DoesNotExist:
            user = None

        if user is not None and user.password==password:
            # User authentication successful, log them in
             
            return redirect('home')  # Redirect to the home page upon successful login # User authentication failed, you can add an error message here if needed
    return render(request,"login.html",{})



def addEvent(request):
    
    return render(request,"addEvent.html",{})
 
def organizerRegistration(request):

     if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST.get('phone', '')
        organization = request.POST.get('organization', '')
        experience = request.POST.get('experience', '')
        event_proposal = request.POST.get('event_proposal', '')
        event_type = request.POST['event_type']
        event_date = request.POST.get('event_date', None)
        event_venue = request.POST.get('event_venue', '')
        budget = request.POST.get('budget', '')
        comments = request.POST.get('comments', '')
        terms = request.POST.get('terms', False)
        if terms == 'on':
            terms = True
        else:
            terms = False

        event_organizer =EventOrganizer(
            fullname=fullname,
            username=username,
            email=email,
            password=password,
            phone=phone,
            organization=organization,
            experience=experience,
            event_proposal=event_proposal,
            event_type=event_type,
            event_date=event_date,
            event_venue=event_venue,
            budget=budget,
            comments=comments,
            terms=terms,
        )
         
        event_organizer.save()

        return redirect('logins')  # Redirect to a success page or another URL
     return render(request,"eventOrganizerRegistration.html",{})

def about(request):

    return render(request,"about.html",{})