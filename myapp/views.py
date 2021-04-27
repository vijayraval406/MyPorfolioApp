from django.shortcuts import render
from .models import Contact
# Create your views here.
def index(request):
	return render(request,'index.html')

def welcome(request):
	return render(request,'welcome.html')

def about(request):
	return render(request,'about.html')

def services(request):
	return render(request,'services.html')

def testimonials(request):
	return render(request,'testimonials.html')

def resume(request):
	return render(request,'resume.html')

def works(request):
	return render(request,'works.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			subject=request.POST['subject'],
			message=request.POST['message'],
			)
		#print(request.POST['name'])
		try:
			msg="Contact Saved Successfully. Will reach You Very Soon.!"
			return render(request,'contact.html',{'msg':msg})
		except Exception as e:
			raise
	else:
		return render(request,'contact.html')