from django.shortcuts import render,HttpResponseRedirect
from blogapp.models import NewsFeed
def home(request):
	data = NewsFeed.objects.all()
	return render(request,'home.html',{'data':data})
def about(request):
	return render(request,'about.html')
def contactform(request):
	return render(request,'contact.html')
