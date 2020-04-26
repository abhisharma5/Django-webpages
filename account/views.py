from django.contrib import messages
from django.shortcuts import render, redirect
from .models import register  #imported

def registration(request):
    if request.method == 'POST':
        fullname = request.POST['fname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if register.objects.filter(Email=email).exists():
                messages.info(request,'username Taken')
                return redirect('../registration/')
            else:
                user=register(Name=fullname,Email=email,Password=password,Cpassword=cpassword)
                user.save()
                print('success')
                return redirect('../login')
        else:
            print('password not matching')
            return redirect('../registration/')
        #return render(request, 'login.html')
    else:
        return render(request,'registration.html')


def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        if register.objects.filter(Email=email,Password=password).exists():
            messages.info(request, 'Logged-In Successfully')
            return redirect('login')
        else:
            return redirect('../registration/')

    else:
        return render(request,'login.html')

