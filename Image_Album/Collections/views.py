from django.contrib import messages
from django.shortcuts import render, redirect
from Collections.forms import ImageForm
from Collections.models import AlbumModel


def add_image(request):
    images = AlbumModel.objects.all()
    form = ImageForm()
    if request.method == 'POST' or request.method == 'FILES':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'one Image Uploaded..!!')
            return redirect('add_image')
    return render(request, 'Album.html',{'form':form,'data':images})

