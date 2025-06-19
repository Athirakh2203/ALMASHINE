from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login 
from .models import Job
from .forms import JobForm,AlumniRegistrationForm
from django.template import TemplateDoesNotExist
import os
from django.conf import settings
from django.contrib.auth import login, authenticate
from .models import Alumni 



def index(request):
    return render(request,"index.html")
def index1(request):
    return render(request,"index1.html")
# Create your views here.
def alumni_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Correctly log in the user
            return render(request,'index1.html')# Redirect to the homepage or dashboard
            
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request,'login.html') 
def Logout(request):
    if request.method == 'POST':
        return render(request,'index.html') 
    else: 
        return render(request,'Logout.html') 
#def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        college = request.POST['college']
        year = request.POST['year']
        
         # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
         # Check if the email is already used
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already used')
            return redirect('register')
       
         # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        # Check if the email is already used
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already used')
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Save additional alumni details in the Alumni model (assuming it exists)
        myreg = Register(user=user, name=name, phone=phone,college=college, year=year)
        myreg.save()
        messages.success(request, 'Registration successful')
        return redirect('login')  # Redirect to the login page after successful registration
    else:
        return render(request, 'register.html')#
    
   
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Alumni


from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import AlumniRegistrationForm

def alumni_register(request):
    if request.method == 'POST':
        form = AlumniRegistrationForm(request.POST, request.FILES)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Please choose a different username.")
                return render(request, 'register.html', {'form': form})

            try:
                # Save the form data
                form.save()
                messages.success(request, "Registration successful. Please log in.")
                return redirect('alumni_login')  # Redirect to login page
            except IntegrityError:
                messages.error(request, "An error occurred while saving your data. Please try again.")
                return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': form})
    
    else:
        form = AlumniRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def event_detail(request, event_id):
    # You can dynamically load event details from a database here
    event_data = {
        1: {
            'title': 'VYVIDH',
            'image': 'events1.jpg',
        },
        2: {
            'title': 'TECTALGIA',
            'image': 'event2.jpg',
            
        },
        3: {
            'title': 'THEJOMAYA',
            'image': 'events3.jpg',
            
        },
        4: {
            'title': 'AARAV',
            'image': 'events4.jpg',
            
        },
        5: {
            'title': 'DHANAK',
            'image': 'events5.jpg',
            
        },
        6: {
            'title': 'THARANG',
            'image': 'events6.jpg',
            
        }
    }
    
    event = event_data.get(event_id, None)
    if event:
        return render(request, 'event_detail.html', {'event': event})
    else:
        return render(request, '404.html')  # You can customize this for a better 404 page
    
def events1(request):
    # Logic to render the 'events1' page
    return render(request, 'events1.html')

def events2(request):
    # Logic to render the 'events1' page
    return render(request, 'events2.html')
def event3(request):
    # Logic to render the 'events1' page
    return render(request, 'event3.html')
def event4(request):
    # Logic to render the 'events1' page
    return render(request, 'event4.html')
def event5(request):
    # Logic to render the 'events1' page
    return render(request, 'event5.html')
def event6(request):
    # Logic to render the 'events1' page
    return render(request, 'event6.html')


def search_alumni(request):
    year = request.GET.get('year')  # Get the 'year' from the URL query parameters
    alumni_list = Alumni.objects.filter(year_of_passout=year) if year else []  # Filter alumni based on year
    
    return render(request, 'search_results.html', {
        'alumni_list': alumni_list,
        'year': year  # Pass the year to the template
    })

def job_post(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Redirect to the job listing page after posting
    else:
        form = JobForm()
    
    return render(request, 'job_post.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})



from .forms import DonationForm

from .forms import DonationForm
from django.urls import reverse

def donation_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save()  # Save the donation to the database
            request.session['donation_id'] = donation.id
            donation_amount = request.POST.get('amount')
            request.session['donation_amount'] = donation_amount  # Store in session
            return redirect(reverse('payment'))  # Redirect to payment page
    else:
        form = DonationForm()

    return render(request, 'donation_page.html', {'form': form})
# views.py
from .forms import PaymentForm



        

            # Send a thank-you email
            

def payment_view(request):
    if request.method == 'POST':
        return redirect('thank_you')  # Proceed to thank you page after "payment"
    return render(request, 'payment.html')

def thank_you(request):
    donation_amount = request.session.get('donation_amount')  # Retrieve from session
    context = {'donation_amount': donation_amount}
    return render(request, 'thank_you.html', context)

def about_us(request):
    return render(request, 'about.html')


from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm
from .models import Review

def review_page(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')  # Redirect to the same page after submission

    # Fetch all reviews to display them on the page
    reviews = Review.objects.all()
    return render(request, 'review_page.html', {'form': form, 'reviews': reviews})