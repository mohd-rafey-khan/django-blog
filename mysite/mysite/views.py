from django.http import HttpResponse
from django.shortcuts import render
import wikipedia

def index(request):
    params ={'name':'None','data':'None'}
    return render(request,'index.html',params)

def blog(request):
    searchdata = request.POST.get('text','default')
    print(searchdata)
    result = wikipedia.summary(searchdata, sentences = 1)
    # print(result)
    params={'name':searchdata,'data':result}
    return render(request,'index.html',params)
