'''Login.views Supports all the user authentication and login and registering process'''
from django.shortcuts import render_to_response, render, redirect
# Takes care of all the basic login, authenticizing and login process for tokenization
from django.contrib.auth import login, logout, authenticate
# The in-built django user module will take care of all the user related database functionality
from django.contrib.auth.models import User
# User of this App
from stockinfo.models import TecStockUser


def login_user(request):
  '''Form support for Login'''
  if request.method == "POST":
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    authenticated = authenticate(username=email, password=password)
    # Valid username and password
    if authenticated and authenticated.is_active:
      login(request, authenticated)
      return redirect('home.html')
    # Incorrect username or password
    else:
      return render(request, 'login/login.html', {'errors': ['Invalid Username and/or Password']})
  else:
    # Display Login Form
    return render(request, 'login/login.html')


def register_user(request):
  '''Form support for User Registration Process'''
  if request.method == "POST":
    # Get POST params from request
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    confirm_password = request.POST.get('password_confirmation', '')
    errors = []
    # Check if the user already exists
    try:
      User.objects.get(username=email)
      errors.append('A user by that username already exists')
    except User.DoesNotExist:
      pass
    # Input Field checks
    if len(password) < 3:
      errors.append('Enter a valid password that is more than 3 characters')
    if password != confirm_password:
      errors.append('Password and Confirm Password don\'t match')
    if len(errors) > 0:
      return render(request, 'login/register.html', {'errors' : errors})
    # Create a User and redirect to login
    user = User.objects.create_user(email, password=password)
    TecStockUser.objects.create(user=user, first_name=first_name, last_name=last_name, email=email)
    return render(request, 'login/login.html')
  else:
    # Display registration form
    return render(request, 'login/register.html')
    

def logout_user(request):
  '''Logout the currently signed user'''
  logout(request)
  return render(request,'home_before_login.html')

def home(request):
  '''Redirects to the Home page'''
  user_id = request.user.id
  cur_user = TecStockUser.objects.filter(user=user_id)[0]
  return render(request, 'home.html',{'user_name': cur_user, 'user':user_id,})

def home_before_login(request):
  return render(request, 'home_before_login.html')

def about(request):
  '''Redirects to the Home page'''
  user_id = request.user.id
  if TecStockUser.objects.filter(user=user_id):
    cur_user = TecStockUser.objects.filter(user=user_id)[0]
    return render(request, 'about.html', {'user_name': cur_user, 'user':user_id,})
  return render(request, 'about.html')

def author(request):
  '''Redirects to the Author page'''
  user_id = request.user.id
  if TecStockUser.objects.filter(user=user_id):
    cur_user = TecStockUser.objects.filter(user=user_id)[0]
    return render(request, 'author.html', {'user_name': cur_user, 'user':user_id,})
  return render(request, 'author.html')
