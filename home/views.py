from django.shortcuts import render
from django.contrib import messages
from .models import Service
from .models import About
from .models import Contact

# Create your views here.
def index(request):
    abouts = About.objects.all()
    services = Service.objects.all()
    return render(request,'index.html',{'abouts':abouts,'services': services})

def contact(request):
    if request.method=="GET":
        return render(request,'contact.html')
    else:    
        postData=request.POST
        name= postData.get('name')
        email=postData.get('email')
        number=postData.get('number')
        message=postData.get('message')
        
    #validation
    value = {
        'name':name,
        'email':email,
        'number':number,
        'msg':message,
    }

    error_message = None
    if(not name):
        error_message="Name is required"
    elif len(name)<5:
        error_message="Please Enter Full Name"    
    
    if len(number)!=10:
        error_message="Please enter Correct number"   

    if not error_message:
        contact=Contact(name=name,email=email,number=number,message=message)
        contact.save()
        messages.success(request,"Sent Succesfully..!")
        return render(request,'contact.html')
        
    
    else:
        data ={
            'error':error_message,
            'value': value,
        }
        return render(request,'contact.html',data)
        

def about(request):
    abouts = About.objects.all()
    return render(request,'about.html',{'abouts':abouts}) 


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

 