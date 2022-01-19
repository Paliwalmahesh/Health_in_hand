from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import  authenticate,login,logout
from Patient_app.models import Address,PatientPasscodes
from Doctor_app.models import DoctorExtra,Prescription
from .decorator import authenticated_user,allowed_users
import joblib
import numpy as np
from laboratory_app.models import Lab_report
from django.views.generic import CreateView
from .forms import DoctorExtraForm,AddressForm



# Create your views here.
def Home(request):
	return render(request,'Doctor_app/Home_bL.html')

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
	
def updateDoctorExtraForm_c(request,username):
	Patient_name = User.objects.get(username=username)
	if request.method == 'POST':
		doctorExtra = DoctorExtra.objects.get(user=Patient_name)
		Address_N=doctorExtra.Address
		form1 = DoctorExtraForm(request.POST,request.FILES, instance=doctorExtra)
		form3 = AddressForm(request.POST,instance=Address_N)
		if form1.is_valid():
			form1.save()
			form3.save()
			return redirect("Doctor_Signin")

	user=Patient_name
	Address_N= Address()
	Address_N.save()
	DoctorExtra_n = DoctorExtra(user=user,Address=Address_N)
	DoctorExtra_n.save()
	doctorExtra = DoctorExtra.objects.get(user=Patient_name)
	form = DoctorExtraForm(instance=doctorExtra)
	Address_N=doctorExtra.Address
	form2=AddressForm(instance=Address_N)
	context = {'form':form,
		'doctorExtra':doctorExtra,
		'form2': form2,}
		
	return render(request, 'Doctor_app/DoctorExtra_form.html', context)
		
	

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
				return redirect("updateDoctorExtraForm_c",username)
		else:
			return render(request,'Doctor_app/Doctor_Signup.html',{'i':'Passwords are not same'})
	else:
		return render(request,'Doctor_app/Doctor_Signup.html')




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
			Prescription_N=Prescription(Doctor_name=Doctor_name,Patient_name=Patient,Prescription_text=Prescription_text,special_advice=special_advice)
			Prescription_N.save()
			return render(request,'Doctor_app/Doctor_index.html',{'i':'Prescription added succesfully!!'})

		else:
			
			return render(request,'Doctor_app/Doctor_Prescription.html',{'i':'Patient is not valid'})
		
	else:
		return render(request,'Doctor_app/Doctor_Prescription.html')

def Heart_health(request):
	forest=joblib.load('static/Heart_health_model.sav')
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
	
		ans = forest.predict(lis)
		if(ans==1):
			txt="you have more than 50 % chanses for heart attack"
		else:
			txt="you have less than 50 % chanses for heart attack"
		return render(request,'Doctor_app/Model_result.html',{'i':txt})
	else:
		return render(request,'Doctor_app/Model_input.html')

def View_Prescription(request):
	if request.method=='POST':
		Patient_name=request.POST['Patient_user_name']
		Patient_Passcode=request.POST['Patient_Passcode']
		if User.objects.filter(username=Patient_name).exists():
			username=User.objects.get(username=Patient_name)
			prescription=Prescription.objects.filter(Patient_name=username)
			patientPasscodes=PatientPasscodes.objects.get(user=username)
			if (Patient_Passcode==patientPasscodes.passcode):
				return render(request,'Doctor_app/view_prescription.html',{'prescription':prescription})
			else:
				return render(request,'Doctor_app/Username_input.html',{'i':"user passcodes is wrong"})  
		else:
			return render(request,'Doctor_app/Username_input.html',{'i':"user does not exits"})   
	else:
		return render(request,'Doctor_app/Username_input.html')

def View_Reports(request):
	if request.method=='POST':
		Patient_name=request.POST['Patient_user_name']
		Patient_Passcode=request.POST['Patient_Passcode']
		if User.objects.filter(username=Patient_name).exists():
			username=User.objects.get(username=Patient_name)
			lab_report=Lab_report.objects.filter(Patient_name=username)
			patientPasscodes=PatientPasscodes.objects.get(user=username)
			if (Patient_Passcode==patientPasscodes.passcode):
				return render(request,'Doctor_app/View_reports.html',{'lab_report':lab_report})
			else:
				return render(request,'Doctor_app/Username_input.html',{'i':"user passcodes is wrong"})  
			
		else: 
			return render(request,'Doctor_app/Username_input.html',{'i':"user does not exits"})  
	else:
		return render(request,'Doctor_app/Username_input.html')
	
def validate_username(request):
	# users = list(User.objects.values_list('username', flat=True))
	# message = "Hello "+username
	# if(username in users):
	#     message = "Username already taken"
	# else:
	#     message = "Username Available"

	if request.method == 'GET':
		users = list(User.objects.values_list('username', flat=True)) 
		username = {'usernames':users}
		# username=request.GET.get('username')
		# message = "Hello "+str(username)
	# return HttpResponse('Url Object Created')
	
		return JsonResponse(username)

def updateDoctorExtraForm(request):
		Patient_name = request.user
		users = User.objects.get(username=Patient_name)
		doctorExtra = DoctorExtra.objects.get(user=users)
		form = DoctorExtraForm(instance=doctorExtra)
		Address_N=doctorExtra.Address
		form2=AddressForm(instance=Address_N)
		if request.method == 'POST':
			form1 = DoctorExtraForm(request.POST,request.FILES, instance=doctorExtra)
			form3 = AddressForm(request.POST,instance=Address_N)
			if form1.is_valid():
				form1.save()
				form3.save()
				return redirect("Doctor_done")
		context = {'form':form,
			'doctorExtra':doctorExtra,
			'form2': form2,}
		return render(request, 'Doctor_app/DoctorExtra_form.html', context)


def View_Prescription_Doc(request,pk):
	Prescription_present=Prescription.objects.filter(Prescriptionid=pk)
	context={
		'Prescription_present':Prescription_present
	}
	return render(request, 'Doctor_app/prescription_template.html', context)

def View_Lab_report_Doc(request,pk):
	Lab_report_present=Lab_report.objects.filter(Lab_reportid=pk)
	context={
		'Lab_report_present':Lab_report_present
	}
	return render(request, 'Doctor_app/Lab_report_template.html', context)

	
	