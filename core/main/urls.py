from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index,name='Index'),
    path('shop/',views.Shop,name='Shop'),
    path('blog/',views.Blog,name='Blog'),
    path('about/',views.About,name='About'),
    
]