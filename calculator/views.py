from django.shortcuts import render
from django.views import View
from .models import Personal

# Create your views here.
class Base(View):
    def get(self,request,*args,**kwargs):
        return render(request,"base.html",{})
    
