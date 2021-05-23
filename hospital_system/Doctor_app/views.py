from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.http import HttpResponse
from django.contrib.auth import  authenticate,login,logout
from Patient_app.models import Address
from Doctor_app.models import DoctorExtra,Prescription
from .decorator import authenticated_user,allowed_users
import joblib
import numpy as np


# Create your views here.
def Home(request):
    return render(request,'Doctor_app/Home.html')

def DoctorHome(request):
    return render(request,'Doctor_app/Doctor_Home.html')

def Doctor_Signin(request):
    if request.method=='POST':
        username = request.POST['usernames']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('Doctor_done')
        else:
            return render(request,'Doctor_app/Doctor_signin.html',{'i':'Invalid username or Password'})

    else:
        return render(request,'Doctor_app/Doctor_signin.html')
    

def Doctor_Signup(request):
    if request.method == 'POST':
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        username = request.POST['username']
        email = request.POST['Email']
        password1 = request.POST['Password']
        password2 = request.POST['Password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                return render(request,'Doctor_app/Doctor_Signup.html',{'i':'user already exsist'})
            else:
                users = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                group = Group.objects.get(name= 'Doctor')
                group.user_set.add(users)
                users.save()
                return redirect('Doctor_Signin')
        else:
             return render(request,'Doctor_app/Doctor_Signup.html',{'i':'Passwords are not same'})
    else:
         return render(request,'Doctor_app/Doctor_Signup.html')


@allowed_users(allowed_roles=['Doctor'])
@authenticated_user 
def Doctor_Extra(request):
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
        DoctorExtra_n = DoctorExtra(user=user,Profilephoto=Profilephoto,Address=Address_N,mobile=mobile)
        DoctorExtra_n.save()
        return HttpResponse("loged in")
    else:
        return render(request,'Doctor_app/DoctorExtra.html')
@allowed_users(allowed_roles=['Doctor'])
@authenticated_user 
def Doctor_done(request):
    return render(request,'Doctor_app/Doctor_index.html')


@allowed_users(allowed_roles=['Doctor'])
@authenticated_user 
def Doctor_Prescription(request):
    username = request.user
    if request.method=='POST':
        Doctor_name=username
        Patient_name=request.POST['Patient_name']
        Prescription_text=request.POST['Prescription_text']
        special_advice=request.POST['special_advice']

        if User.objects.filter(username=Patient_name).exists():
            Patient=User.objects.get(username=Patient_name)
            # group = request.user.groups.filter(name=Patient)
            Prescription_N=Prescription(Doctor_name=Doctor_name,Patient_name=Patient,Prescription_text=Prescription_text,special_advice=special_advice)
            Prescription_N.save()
            return redirect('Doctor_done')
        else:
            
            return render(request,'Doctor_app/Doctor_Prescription.html',{'i':'Patient is not valid'})
        
    else:
        return render(request,'Doctor_app/Doctor_Prescription.html')

def Heart_health(request):
    forest=joblib.load('Heart_health_model.sav')
    if request.method=='POST':
        lis=np.array([])
        lis=np.append(lis,request.POST['age'])
        lis=np.append(lis,request.POST['Gender'])
        lis=np.append(lis,request.POST['Height'])
        lis=np.append(lis,request.POST['Weight'])
        lis=np.append(lis,request.POST['ap_hi'])
        lis=np.append(lis,request.POST['ap_low'])
        lis=np.append(lis,request.POST['Cholestrol'])
        lis=np.append(lis,request.POST['Glucose'])
        lis=np.append(lis,request.POST['smoke'])
        lis=np.append(lis,request.POST['Alocohol'])
        lis=np.append(lis,request.POST['Active'])
        lis=lis.reshape(1,11)
        print(lis)
        ans = forest.predict(lis)
        if(ans==1):
            txt="you have more than 50 % chanses for heart attack"
        else:
            txt="you have less than 50 % chanses for heart attack"
        return render(request,'Doctor_app/Model_result.html',{'i':txt})
    else:
        return render(request,'Doctor_app/Model_input.html')