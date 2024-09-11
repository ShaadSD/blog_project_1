from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form=forms.Post(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form=forms.Post()
    return render (request,'add_post.html',{'form':post_form})

def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    post_form=forms.Post(instance=post)
    if request.method == 'POST':
        post_form=forms.Post(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    return render (request,'add_post.html',{'form':post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id) 
    post.delete()
    return redirect('homepage')