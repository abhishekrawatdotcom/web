from django.shortcuts import render


def webview(request):
    return render(request,'web.html')

def inview(request):
    return render(request,'in.html')
# Create your views here.
