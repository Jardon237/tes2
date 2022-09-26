
from email import contentmanager, message
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import MyForm

def home(request):
    form = Myform()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save
            return HttpResponse('thanks for your your submission')
    context ={
        'form': form
    }
        
    return render(request, 'home.html', context)



def sigup(request):


    if request.method == 'POST':

        username= request.POST.get('username')
        fname= request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1', False)
        pass2 = request.POST.get('pass2', False)

        my_user = User.objects.create_user(username , email, pass1)

        my_user.save()
        return HttpResponse
        (request,"Your Account has been created.")
        return redirect('signin')
    
        
    
    return render(request, 'sigup.html')  
def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username = username, password= pass1)

        if user is not None:
            login(request, user)
            user = user.get_username
            return render(request, 'home.html')
        else:
            messages.error(request, 'wrong details')
            return redirect('signin')

    return render(request, 'signin.html')

def seat(request):
    return render(request, 'seat.html')

def available(request):
    return render(request, 'available.html')

def about(request):
    return render(request, 'about.html')