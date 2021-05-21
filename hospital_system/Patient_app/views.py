from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.http import HttpResponse
from django.contrib.auth import  authenticate,login,logout
from .models import PatientExtra,Address
from Doctor_app.models import Prescription
from laboratory_app.models import Lab_report
from Doctor_app.decorator import allowed_users,authenticated_user




def PatientHome(request):
    return render(request,'Patient_app/Patient_Home.html')

def Patient_Signin(request):
    if request.method=='POST':
        username = request.POST['usernames']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('Patient_done')
        else:
            return render(request,'Patient_app/Patient_signin.html',{'i':'Invalid username or Password'})

    else:
        return render(request,'Patient_app/Patient_signin.html')
    

def Patient_Signup(request):
    if request.method == 'POST':
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        username = request.POST['username']
        email = request.POST['Email']
        password1 = request.POST['Password']
        password2 = request.POST['Password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                return render(request,'Patient_app/Patient_Signup.html',{'i':'user already exsist'})
            else:
                users = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                group = Group.objects.get(name= 'Patient')
                group.user_set.add(users)
                users.save()
                return redirect('Patient_Signin')
        else:
             return render(request,'Patient_app/Patient_Signup.html',{'i':'Passwords are not same'})
    else:
         return render(request,'Patient_app/Patient_Signup.html')

@allowed_users(allowed_roles=['Patient,Admin'])
@authenticated_user 
def Patient_Extra(request):
    username = request.user
    if request.method == 'POST':
        user=username
        mobile = request.POST['Phonenumber']
        Place_name = request.POST['Place_name']
        city= request.POST['city']
        state= request.POST['state']
        pincode = request.POST['pincode']
        Profilephoto = request.POST['fileToUpload']
        Address_N= Address(Place_name=Place_name,city=city,state=state,pincode=pincode)
        Address_N.save()
        PatientExtra_n = PatientExtra(user=user,Profilephoto=Profilephoto,Address=Address_N,mobile=mobile)
        PatientExtra_n.save()
        return HttpResponse("loged in")
    else:
        return render(request,'Patient_app/PatientExtra.html')

@allowed_users(allowed_roles=['Patient,Admin'])
@authenticated_user 
def Patient_done(request):
    return render(request,'Patient_app/Patient_index.html')

@allowed_users(allowed_roles=['Patient,Admin'])
@authenticated_user 
def Patient_Prescription(request):
    username = request.user
    prescription=Prescription.objects.filter(Patient_name=username)
    return render(request,'Patient_app/Patient_Prescription.html',{'prescription':prescription})

@allowed_users(allowed_roles=['Patient,Admin'])
@authenticated_user 
def Patient_Report(request):
    username = request.user
    lab_report=Lab_report.objects.filter(Patient_name=username)
    return render(request,'Patient_app/Patient_Lab_report.html',{'lab_report':lab_report})