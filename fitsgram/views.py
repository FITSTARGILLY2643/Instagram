from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comment
from django.contrib.auth.models import User
from .forms import NewImageForm,CommentForm,ProfileForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import json

# Create your views here.
@login_required(login_url='accounts/login/')
def index(request):
    if request.user.is_superuser:
        return redirect('http://localhost:8000/admin')
    else:
        images = Image.get_images()
        comments = Comment.objects.all()
        form = CommentForm()
        return render(request,"index.html",{"images":images,"form":form,"comments":comments})
