
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
from taggit.models import Tag


# Create your views here.




def home(request):
      
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    
    allfonts = Fonts.objects.filter(publish = True)
    alltag = Tag.objects.all()
    p = Paginator(allfonts, 8)
    page = request.GET.get('page')
    fontsfinal = p.get_page(page)
    topfonts = Fonts.objects.order_by('-Total_downloads')
    

    context = {'fontsfinal': fontsfinal,                
                'copyright': copyright,
                'websitedata': websitedata,
                'topfonts': topfonts[:2],
                'alltag': alltag
    
    }
    return render(request , 'index.html',context)  

    



def allfonts(request):
    alltag = Tag.objects.all()
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    allfonts = Fonts.objects.filter(publish = True)
    p = Paginator(allfonts, 5)
    page = request.GET.get('page')
    fontsfinal = p.get_page(page)
    

    context = {'fontsfinal': fontsfinal,
               'title': 'all fonts',
               'websitedata': websitedata, 
               'alltag': alltag,
                
    }

    return render(request , 'allfonts.html',context)


def fonts_details(request, slug):

    

     
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    allfonts = Fonts.objects.order_by('-Total_downloads')
    title = Fonts.objects.filter(slug = slug).first()
    alltag = Tag.objects.filter(slug = slug).first()
    
    context = {
        'allfonts': allfonts[:2],
        'title': title,
        'websitedata': websitedata, 
        'copyright': copyright,
        'alltag': alltag,
        
        
    }
    try:
        fonts_obj = Fonts.objects.filter(slug = slug).first()
        context['fonts_obj'] = fonts_obj
    except Exception as e:
        print(e) 

        
        
    return render(request , 'fonts_details.html' , context)



def contact(request):
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    context = {
        
        'websitedata': websitedata,
        
        
        
    }


    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name, email, subject, message)
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, "your message has been send to us")
        return redirect('/')
        
    
    return render(request , 'contact.html', context )   
         
    



def termsandcondition(request):

    
    discription = Pages.objects.latest('termsandcondition')
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )

    context = {
        'discription': discription,
        'websitedata': websitedata,
        
        
        
    }
    return render(request, 'termsandcondition.html', context)


def privacypolicy(request):
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    discription = Pages.objects.latest('privacypolicy')
    context = {'discription': discription, 'websitedata': websitedata,}  
    return render(request, 'privacypolicy.html', context)




    
def pages(request):
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    discription = Pages.objects.latest('ourpages')
    context = {'discription': discription, 'websitedata': websitedata,} 
    return render(request, 'pages.html', context)

def aboutus(request):
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    discription = Pages.objects.latest('aboutus')
    context = {'discription': discription, 'websitedata': websitedata,} 
    return render(request, 'aboutus.html', context)





def help(request):     
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    context = {        
                'websitedata': websitedata
    
    }
    return render(request , 'help.html',context)  

def linux(request):     
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    context = {        
                'websitedata': websitedata
    
    }
    return render(request , 'linux.html',context)  

def windows(request):     
    websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
    context = {        
                'websitedata': websitedata
    
    }
    return render(request , 'windows.html',context) 


def search(request): 
    if request.method == "POST": 
        searched = request.POST['searched'] 
        searchfonts = Fonts.objects.filter(title__contains=searched)
        
       

        websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
        context = { 
                       
                'websitedata': websitedata,
                'searched': searched,
                'searchfonts': searchfonts,
                
    
                }
        return render(request , 'search.html',context)

    else:
        websitedata = Modification.objects.latest('websitename', 'websitediscription', 'ouremail', 'copyright', 'logo', 'favicon' )
        context = {        
                'websitedata': websitedata
    
                }
        return render(request , 'search.html',context)
robots_file = '''User-Agent: *
Disallow:
Allow: /

Sitemap: https://arabfonts.org/sitemap.xml
'''

def robots(request):
    content = robots_file
    return HttpResponse(content, content_type='text/plain')
     