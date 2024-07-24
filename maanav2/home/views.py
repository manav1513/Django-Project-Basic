from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
    context = {
        'title':'Home Page',
        'content':'Welcome to our home page'
    }
    messages.success(request , "successful")
    return render(request,'index.html', context)
#return HttpResponse("this is home page")

def about(request):
    return HttpResponse("this is the about page")

def contact(request):
    if request.method == "POST":
        print("this function is runnign ")
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        contact = contact(name = name , phone = phone , address = address)
        print(contact)

        contact.save()
    return render(request, 'contact.html')

def postcontact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        data = Contact(name = name ,phone = phone , address = address)
        data.save() 
        messages.success(request , "successful")
        response = redirect('/contact/')
    return response
def man(request):
    return HttpResponse("this is man page")