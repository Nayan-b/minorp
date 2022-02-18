from django.shortcuts import render
from .models import Image
from .form import ImageForm
# Create your views here.


def home(request):
    return render(request, 'sign/sign.html')


def verify(request):
    verification = False
    imagefile = None
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        imagefile = form.cleaned_data['imagefile']
        name = form.cleaned_data['name']
        print('VAlid')
        # chech the input signature with the signature in the database


        # if match:
        #     print('Match')
        # else:
        #     print('Not Match')
        verification = True
    else:
        print('Invalid')
    
    
    context = {
               'form': form,
               'imagefile': imagefile,
               'verification': verification
               }

    return render(request, 'sign/verify.html', context)


def upload(request):

    
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print('Valid')
        form.save()


    context = {'form': form}

    return render(request, 'sign/upload.html', context)
