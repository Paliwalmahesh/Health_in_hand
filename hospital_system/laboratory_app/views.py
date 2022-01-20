from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.http import HttpResponse
from django.contrib.auth import  authenticate,login,logout
from .models import Lab_report,LaboratoryExtra
from Doctor_app.forms import AddressForm
from Patient_app.models import Address,PatientPasscodes
from .forms import LaboratoryExtraForm
from Doctor_app.decorator import allowed_users,authenticated_user

# Create your views here.
def LaboratoryHome(request):
    return render(request,'laboratory_app/Laboratory_Home.html')

def updateLaboratoryExtraForm_c(request,username):
	Patient_name = User.objects.get(username=username)
	try:
		if request.method == 'POST':
			laboratoryExtra = LaboratoryExtra.objects.get(user=Patient_name)
			Address_N=laboratoryExtra.Address
			form1 = LaboratoryExtraForm(request.POST,request.FILES, instance=laboratoryExtra)
			form3 = AddressForm(request.POST,instance=Address_N)
			if form1.is_valid():
				form1.save()
				form3.save()
				return redirect("Laboratory_Signin")

		user=Patient_name
		Address_N= Address()
		Address_N.save()
		LaboratoryExtra_n = LaboratoryExtra(user=user,Address=Address_N)
		LaboratoryExtra_n.save()
		laboratoryExtra = LaboratoryExtra.objects.get(user=Patient_name)
		form = LaboratoryExtraForm(instance=laboratoryExtra)
		Address_N=laboratoryExtra.Address
		form2=AddressForm(instance=Address_N)
		context = {'form':form,
			'laboratoryExtra':laboratoryExtra,
			'form2': form2,}
		return render(request, 'Laboratory_app/LaboratoryExtra_form.html', context)
	except:
		return render(request,'Laboratory_app/Laboratory_signin.html',{'i':'Login & update'})

def Laboratory_Signup(request):
    if request.method == 'POST':
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        username = request.POST['username']
        email = request.POST['Email']
        password1 = request.POST['Password']
        password2 = request.POST['Password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                return render(request,'Laboratory_app/Laboratory_Signup.html',{'i':'user already exsist'})
            else:
                users = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                group = Group.objects.get(name= 'Laboratory')
                group.user_set.add(users)
                users.save()
                return redirect('updateLaboratoryExtraForm_c',username)
        else:
             return render(request,'Laboratory_app/Laboratory_Signup.html',{'i':'Passwords are not same'})
    else:
         return render(request,'Laboratory_app/Laboratory_Signup.html')

def Laboratory_Signin(request):
    if request.method=='POST':
        username = request.POST['usernames']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('Laboratory_done')
        else:
            return render(request,'Laboratory_app/Laboratory_signin.html',{'i':'Invalid username or Password'})

    else:
        return render(request,'Laboratory_app/Laboratory_signin.html')


@allowed_users(allowed_roles=['Laboratory'])
@authenticated_user        
def Laboratory_done(request):
    return render(request,'Laboratory_app/Laboratory_index.html')

@allowed_users(allowed_roles=['Laboratory'])
@authenticated_user 
def Laboratory_report(request):
    username = request.user
    if request.method=='POST':
        Laboratory_name=username
        Doctor_name=request.POST['Doctor_name']
        Patient_name=request.POST['Patient_name']
        Test_name=request.POST['Test_name']
        report_text=request.POST['report_text']
        if User.objects.filter(username=Patient_name).exists():
            if User.objects.filter(username=Doctor_name).exists():
                Patient=User.objects.get(username=Patient_name)
                Doctor=User.objects.get(username=Doctor_name)
                Lab_report_N=Lab_report(Laboratory_name=Laboratory_name,Doctor_name=Doctor,Patient_name=Patient,Test_name=Test_name,report_text=report_text)
                Lab_report_N.save()
                return render(request,'Laboratory_app/Laboratory_index.html',{'i':'Report added successfully !!'})
            else:
                return render(request,'Laboratory_app/Laboratory_reports.html',{'i':'Doctor name  is not valid'})
        else:
            return render(request,'Laboratory_app/Laboratory_reports.html',{'i':'Patient name is not valid'})
    else:
        return render(request,'Laboratory_app/Laboratory_reports.html')

@allowed_users(allowed_roles=['Laboratory'])
@authenticated_user 
def updateLaboratoryExtraForm(request):
		Patient_name = request.user
		users = User.objects.get(username=Patient_name)
		laboratoryExtra = LaboratoryExtra.objects.get(user=users)
		form = LaboratoryExtraForm(instance=laboratoryExtra)
		Address_N=laboratoryExtra.Address
		form2=AddressForm(instance=Address_N)
		if request.method == 'POST':
			form1 = LaboratoryExtraForm(request.POST,request.FILES, instance=LaboratoryExtra)
			form3 = AddressForm(request.POST,instance=Address_N)
			if form1.is_valid():
				form1.save()
				form3.save()
				return redirect("Laboratory_done")
		context = {'form':form,
			'laboratoryExtra':laboratoryExtra,
			'form2': form2,}
		return render(request, 'Laboratory_app/LaboratoryExtra_form.html', context)

@allowed_users(allowed_roles=['Laboratory'])
@authenticated_user 
def View_Reports_lab(request):
	if request.method=='POST':
		Patient_name=request.POST['Patient_user_name']
		Patient_Passcode=request.POST['Patient_Passcode']
		if User.objects.filter(username=Patient_name).exists():
			username=User.objects.get(username=Patient_name)
			lab_report=Lab_report.objects.filter(Patient_name=username)
			patientPasscodes=PatientPasscodes.objects.get(user=username)
			if (Patient_Passcode==patientPasscodes.passcode):
				return render(request,'Laboratory_app/View_reports.html',{'lab_report':lab_report})
			else:
				return render(request,'Laboratory_app/Username_input.html',{'i':"user passcodes is wrong"})  
			
		else: 
			return render(request,'Laboratory_app/Username_input.html',{'i':"user does not exits"})  
	else:
		return render(request,'Laboratory_app/Username_input.html')
	
@allowed_users(allowed_roles=['Laboratory'])
@authenticated_user 
def View_Lab_report_Lab(request,pk):
	Lab_report_present=Lab_report.objects.filter(Lab_reportid=pk)
	context={
		'Lab_report_present':Lab_report_present
	}
	return render(request, 'Doctor_app/Lab_report_template.html', context)

	
	