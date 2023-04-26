from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

from .functions import *
# Create your views here.

@login_required(login_url='/')
def keyword_researcher(request):
    template_name='keywordresearch.html'
    if request.method=="POST":
        keyword=request.POST.get('keyword')
        layout=request.POST.get('layout')
        related=Layout_related(keyword,int(layout))
        sugesstion=getGoogleSuggests(keyword)
        create_exel(keyword,sugesstion,'Sugessted keyword',related,'Related keyword')
        context={

        }
        return render(request,template_name,context)

    context={}

    return render(request,template_name,context)

