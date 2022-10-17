from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from new_app.forms import LoginForm, SignUpForm, VehicleForm
from new_app.models import VehicleModel

# Create your views here.


def Registration(request):
    message = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            message = 'Account Created Successfully'
            return redirect('login_view')
        else:
            message = 'Form is Invalid'
    else:
        form = SignUpForm()
    return render(request,'register.html',{'form':form,'message':message})


def login_view(request):
    form = LoginForm(request.POST)
    message = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                print(user.is_user)
                print(user.is_admin)
                print(user.is_superuser)
                if user.is_user:
                    return redirect('user')
                if user.is_admin:
                    return redirect('admin_view')
                if user.is_superuser:
                    return redirect('superuser')
                return redirect('home')
            else:
                message = 'Invalid Credentials'
        else:
            message = 'Form is Inavlid'

    return render(request,'login.html',{'form':form,'message':message})



def home(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

def user_view(request):
    data = VehicleModel.objects.all()
    return render(request,'user.html',{'data':data})

def admin_view(request):
    data = VehicleModel.objects.all()
    return render(request,'admin.html',{'data':data})

def superuser_view(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('superuser')
    else:
        form = VehicleForm()
    data = VehicleModel.objects.all()

    return render(request,'superuser.html',{'data':data,'form':form})

def edit_view(request,pk):
    data = VehicleModel.objects.get(pk=pk)
    print(request.user)
    if request.method == 'POST':

        vehicle_number = request.POST['vehicle_number']
        vehicle_model = request.POST['vehicle_model']
        vehicle_type = request.POST['vehicle_type']
        vehicle_description = request.POST['vehicle_description']

        data.vehicle_number = vehicle_number
        data.Vehicle_type = vehicle_type
        data.vehicle_model = vehicle_model
        data.vehicle_description = vehicle_description

        data.save()
        if request.user.is_superuser:
            return redirect('superuser')
        if request.user.is_admin:
            return redirect('admin_view')

    return render(request,'edit.html',{'data':data})

def delete_view(request,pk):
    data = VehicleModel.objects.get(pk=pk)
    data.delete()
    message = "Data Deleted Successfully !"
    return render(request,'home.html',{'message':message})