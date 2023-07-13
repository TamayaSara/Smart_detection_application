from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def uploadImageView(request): 
    if request.method =='POST':
        image_upload = request.FILES['file']
    
    test = 'String'

    context = {
        'test':test,
    }

   # return render(request,'media/uploadImage.html', context)

    return render(request, '/Users/tamayasara/AI_Hackathon/AI_Hackathon/templates/uploadImage.html', context)
# Create your views here.
