from django.urls import path
from .views import *

urlpatterns = [
    path('' , home , name="home"),
    path('allfonts' , allfonts , name="allfonts"),
    path('<slug:slug>/' , fonts_details , name="fonts_details"),
    path('contact' , contact , name="contact"),
    path('termsandcondition' , termsandcondition , name="termsandcondition"),
    path('privacypolicy' , privacypolicy , name="privacypolicy"),
    path('pages' , pages , name="our_page"),
    path('aboutus' , aboutus , name="aboutus")
 
    

]