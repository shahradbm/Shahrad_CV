from django.shortcuts import render
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'cv_app/index.html' , { 
        'name' : 'shahrad' , 
        'lastname' : 'beyg mohammadi' , 
        'position' : 'Founder' , 
        'profile': settings.MEDIA_URL + 'shahrad/me.jpg',
        'email' : 'shahradbm952@gmail.com',
        'Birthday' : '27 september 2009' ,
        'Age' : '15' ,
        'Languages': 'English, Persian, German' , 
        'Phone' : '+98 919 803 6004', 
        'city' : 'tehran, iran' ,
        'Certification' : 'Python Specialist' ,
        'Institution' : 'Maktabkhooneh' ,
        'year' : '1403' ,
        'dicription' : 'I am a python developer and currently working with html as well.' ,
        'web' : 'www.yarnico.com',
        'Freelance' : 'Available',
        
        }) 
