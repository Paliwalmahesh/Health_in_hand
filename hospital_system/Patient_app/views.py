from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.http import HttpResponse
from django.contrib.auth import  authenticate,login,logout
from Patient_app.models import Address,PatientPasscodes,PatientExtra
from .forms import PatientExtraForm,PatientPasscodesForm
from Doctor_app.forms import AddressForm
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
def updatePatientExtraForm_c(request,username):
	Patient_name = User.objects.get(username=username)
	if request.method == 'POST':
		patientExtra = PatientExtra.objects.get(user=Patient_name)
		Address_N=patientExtra.Address
		form1 = PatientExtraForm(request.POST,request.FILES, instance=patientExtra)
		form3 = AddressForm(request.POST, instance=Address_N)
		form5=PatientPasscodesForm(request.POST,instance=Patient_name)
		if form1.is_valid():
			form1.save()
			form3.save()
			form5.save()
			return redirect("Patient_Signin")
	Address_N= Address()
	Address_N.save()
	PatientExtran = PatientExtra(user=Patient_name,Address=Address_N)
	PatientExtran.save()
	patientExtra = PatientExtra.objects.get(user=Patient_name)
	form = PatientExtraForm(instance=patientExtra)
	Address_N=patientExtra.Address
	form2=AddressForm(instance=Address_N)
	PatientPasscodesForm_n=PatientPasscodes(user=Patient_name)
	PatientPasscodesForm_n.save()
	form4=PatientPasscodesForm(instance=Patient_name)
	context = {'form':form,
		'form4':form4,
		'PatientExtra':patientExtra,
		'form2': form2,}
	return render(request, 'Patient_app/PatientExtra_form.html', context)

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
				return redirect('updatePatientExtraForm_c',username)
		else:
			 return render(request,'Patient_app/Patient_Signup.html',{'i':'Passwords are not same'})
	else:
		 return render(request,'Patient_app/Patient_Signup.html')

@allowed_users(allowed_roles=['Patient'])
def Patient_done(request):
	return render(request,'Patient_app/Patient_index.html')

@allowed_users(allowed_roles=['Patient'])

def Patient_Prescription(request):
	username = request.user
	prescription=Prescription.objects.filter(Patient_name=username)
	return render(request,'Patient_app/Patient_Prescription.html',{'prescription':prescription})

@allowed_users(allowed_roles=['Patient'])
def Patient_Report(request):
	username = request.user
	lab_report=Lab_report.objects.filter(Patient_name=username)
	return render(request,'Patient_app/Patient_Lab_report.html',{'lab_report':lab_report})

def View_Prescription_user(request,pk):
	Prescription_present=Prescription.objects.filter(Prescriptionid=pk)
	context={
		'Prescription_present':Prescription_present
	}
	return render(request, 'Doctor_app/prescription_template.html', context)

def View_Lab_report_user(request,pk):
	Lab_report_present=Lab_report.objects.filter(Lab_reportid=pk)
	context={
		'Lab_report_present':Lab_report_present
	}
	return render(request, 'Doctor_app/Lab_report_template.html', context)

def updatePatientExtraForm(request):
		Patient_name = request.user
		users = User.objects.get(username=Patient_name)
		patientExtra = PatientExtra.objects.get(user=users)
		form = PatientExtraForm(instance=patientExtra)
		Address_N=patientExtra.Address
		form2=AddressForm(instance=Address_N)
		Patient_Passcode=PatientPasscodes.objects.get(user=users)
		form4=PatientPasscodesForm(instance=Patient_Passcode)
		if request.method == 'POST':
			form1 = PatientExtraForm(request.POST,request.FILES, instance=patientExtra)
			form3 = AddressForm(request.POST,instance=Address_N)
			form5=PatientPasscodesForm(request.POST,instance=Patient_name)
			if form1.is_valid():
				form1.save()
				form3.save()
				form5.save()
				return redirect("Patient_done")
		context = {'form':form,
				'form4':form4,
			'PatientExtra':patientExtra,
			'form2': form2,}
		return render(request, 'Patient_app/PatientExtra_form.html', context)