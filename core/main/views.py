from django.shortcuts import render
from .models import slider,product,about,offer,offer_s,blog,client

# Create your views here.

def Index(request):
    slider_list = slider.objects.all()
    prod_list = product.objects.all()
    about_list = about.objects.all()
    offer_list = offer.objects.all()
    offer_s_list = offer_s.objects.all()
    blog_list = blog.objects.all()
    client_list = client.objects.all()
    return render(request,'main/index.html',context={
        'slider_list':slider_list,
        'prod_list':prod_list,
        'about_list':about_list,
        'offer_list':offer_list,
        'offer_s_list':offer_s_list,
        'blog_list':blog_list,
        'client_list':client_list,
    })

def Shop(request):
    return render(request,'main/shop.html')

def Blog(request):
    return render(request,'main/blog.html')

def About(request):
    return render(request,'main/about.html')