from django.shortcuts import render
from .models import Image
from .form import ImageForm
# Create your views here.


def home(request):
    return render(request, 'sign/sign.html')


def upload(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
    else:
        return render(request, 'sign/upload.html')


def verify(request):
    return render(request, 'sign/verify.html')


def showimage(request):

    lastimage = Image.objects.last()
    imagefile = None
    # imagefile= lastimage.imagefile
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

    context = {'imagefile': imagefile,
               'form': form}

    return render(request, 'sign/upload.html', context)
