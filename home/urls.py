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
    path('aboutus' , aboutus , name="aboutus"),
    path('fonts' , home , name="arabic fonts"),
    path('help' , help , name="help"),
    path('install-fonts-on-linux', linux , name="install_fonts_on_linux"),
    path('install-fonts-on-windows', windows , name="install_fonts_on_windows"),
    path('search' , search , name="search"),
    path('robots.txt', robots, name='robots'),
 
    

]