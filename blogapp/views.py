from django.shortcuts import render
from django.http import HttpResponseRedirect
from blogapp.forms import SignupUser,LoginForm,PostFeed,UserEditForm,PasswordEditForm,ProfileEditForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from blogapp.models import NewsFeed
from django.contrib.auth.forms import User,PasswordChangeForm
from django.contrib import messages

# Create your views here.
def signupform(request):
	if request.method == 'POST':
		fm = SignupUser(request.POST)
		if fm.is_valid():
			fm.save()
			messages.info(request,'Signin Successful now Login')
			return HttpResponseRedirect('/blogapp/login')
	else:
		fm = SignupUser()
	return render(request,'signup.html',{'frm':fm})

def loginform(request):

	if not request.user.is_authenticated:
		if request.method == 'POST':
			fm = LoginForm(request=request,data=request.POST)
			
			if fm.is_valid():
				uname = fm.cleaned_data.get('username')
				upass = fm.cleaned_data.get('password')
				
				user = authenticate(username=uname,password=upass)

				if user is not None:
					login(request,user)
					if request.user.is_superuser :
						messages.info(request,'Logged in Successfully')
						return HttpResponseRedirect('/blogapp/dash')
					else:
						return HttpResponseRedirect('/blogapp/commonuser')
		else:
			fm = LoginForm()
		return render(request,'login.html',{'frm':fm})

	else:
		return HttpResponseRedirect('/blogapp/dash')
		

def dashboard(request):
	if request.user.is_authenticated:
		if request.user.is_superuser or request.user.is_staff :
			data = NewsFeed.objects.all()
			return render(request,'dashboard.html',{'data':data})
		else:
			return HttpResponseRedirect('/blogapp/commonuser')
	else:
		return HttpResponseRedirect("/blogapp/login")

def logzout(request):
	logout(request)
	return HttpResponseRedirect('/blogapp/login')

def addpost(request):
	if request.user.is_authenticated:
		if request.user.is_superuser or request.user.is_staff:
			if request.method == 'POST':
				fm = PostFeed(request.POST)
				if fm.is_valid:
					fm.save()
					return HttpResponseRedirect('/blogapp/dash')
			else:
				fm = PostFeed()
			return render(request,'addpost.html',{'frm':fm})
		else:
			return HttpResponseRedirect('/blogapp/commonuser')
	else:
		return HttpResponseRedirect('/blogapp/login')

def editfeed(request,id):
	if request.user.is_authenticated:
		if request.user.is_superuser or request.user.is_staff:
			if request.method == 'POST':
				data = NewsFeed.objects.get(pk=id)
				fm = PostFeed(instance=data,data=request.POST)
				if fm.is_valid():
					fm.save()
					return HttpResponseRedirect('/blogapp/dash')
			else:
				data = NewsFeed.objects.get(pk=id)
			fm = PostFeed(instance=data)
			return render(request,'editfeed.html',{'frm':fm})
		else:
			HttpResponseRedirect('/blogapp/commonuser')
	else:
		return HttpResponseRedirect('/blogapp/login')
		
def deletez(request,id):
	if request.user.is_authenticated:
		if request.user.is_superuser:
			data = NewsFeed.objects.get(pk=id)
			data.delete()
			return HttpResponseRedirect('/blogapp/dash')
		else:
			return HttpResponseRedirect('/blogapp/commonuser')
	else:
		return HttpResponseRedirect('/blogapp/login')

def memberz(request):
	if request.user.is_authenticated:
		if request.user.is_superuser:
			fm = User.objects.all()
			return render(request,'members.html',{'frm':fm})
		else:
			return HttpResponseRedirect('/blogapp/commonuser')
	else:
		return HttpResponseRedirect('/blogapp/login')
	
	
def editmember(request,id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			data = User.objects.get(pk=id)
			fm = UserEditForm(request.POST,instance=data)
			if fm.is_valid():
				fm.save()
				return HttpResponseRedirect('/blogapp/members')
				
		data = User.objects.get(pk=id)
		fm = UserEditForm(instance=data)
		return render(request,'editmember.html',{'frm':fm,'data':data})
	else:
		return HttpResponseRedirect('/blogapp/login')

def deletemember(request,id):
	if request.user.is_authenticated:
		if request.user.is_superuser:
			data = User.objects.get(pk=id)
			data.delete()
			return HttpResponseRedirect('/blogapp/members')
		else:
			return HttpResponseRedirect('/blogapp/commonuser')
	else:
		return HttpResponseRedirect('/blogapp/login')
	
def commonuser(request):
	if request.user.is_authenticated:
		return render(request,'commonusers.html')
	else:
		return HttpResponseRedirect('/blogapp/login')
	
def editpassword(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			pc = PasswordEditForm(user=request.user,data=request.POST)
			if pc.is_valid():
				pc.save()
				update_session_auth_hash(user=request.user)
				return HttpResponseRedirect('/blogapp/login')
		else:
			pc = PasswordEditForm(request.user)
			return render(request,'editpassword.html',{'pcf':pc})
	else:
		return HttpResponseRedirect('/blogapp/login')
	
def profileedit(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			fm = ProfileEditForm(request.POST,instance=request.user)
			if fm.is_valid():
				fm.save()
				messages.info(request,'Profile Updated')
				return HttpResponseRedirect('/blogapp/commonuser')
		else:
			fm = ProfileEditForm(instance=request.user)
		return render(request,'profileedit.html',{'frm':fm})
	else:
		return HttpResponseRedirect('/blogapp/login')

