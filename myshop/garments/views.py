from django.shortcuts import render,get_object_or_404,get_list_or_404
from garments.models import FormalShirt
from garments.models import CasualShirt
from garments.models import TShirt
from garments.models import Trousers
from garments.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')

def formal_shirts(request):
    lst=FormalShirt.objects.all()
    return render(request,"formal_shirts.html",{'lst':lst})


def casual_shirts(request):
    lst=CasualShirt.objects.all()
    return render(request,"casual_shirts.html",{'lst':lst})

def t_shirts(request):
    lst=TShirt.objects.all()
    return render(request,"t_shirts.html",{'lst':lst})

def trousers(request):
    lst=Trousers.objects.all()
    return render(request,"Trousers.html",{'lst':lst})


def contactus(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        subject='hello from garments.com'
        message='this is what you typed:'+request.POST.get('content')
        from_email=settings.EMAIL_HOST_USER
        user_email=request.POST.get('contact_email')
        to_list=[user_email,settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')
    return render(request, 'contactus.html',{'form':form})

def thankyou(request):
    res=HttpResponse()
    res.write("<h1> Thankyou for visiting site </h1>")
    res.write("<h1> we just sent a mail to you </h1>")
    res.write("<h1> please go through it.</h1>")
    return res
lst=[]
price=[]
def cart(request,x):
    item=get_object_or_404(FormalShirt,pk=x)
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'tot_price':sum(price)})

lst=[]
price=[]
def cart(request,x):
    item=get_object_or_404(CasualShirt,pk=x)
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'tot_price':sum(price)})

lst=[]
price=[]
def cart(request,x):
    item=get_object_or_404(TShirt,pk=x)
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'tot_price':sum(price)})





lst=[]
price=[]
def cart(request,x):
    item=get_object_or_404(Trousers,pk=x)
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'tot_price':sum(price)})


