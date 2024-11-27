from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseForbidden
from django.views import View



# Create your views here.
class Index(View):
    def get(self,request):
        # return render(request,'index.html')
        cookie = request.COOKIES  # cookie是一个字典

        ussername = cookie.get('username')
        counst = {
            'username': ussername
        }

        return render(request,'index.html',counst)
    def post(self,request):

        return HttpResponse('post')

def zixun(request):
    cookie = request.COOKIES  # cookie是一个字典

    ussername = cookie.get('username')
    counst = {
        'username': ussername
    }
    return render(request,'zixun.html',counst)
def kepu(request):
    cookie = request.COOKIES  # cookie是一个字典

    ussername = cookie.get('username')
    counst = {
        'username': ussername
    }
    return render(request,'kepu.html',counst)


def news1(request):
    cookie = request.COOKIES  # cookie是一个字典

    ussername = cookie.get('username')
    counst = {
        'username': ussername
    }
    return render(request,'news1.html',counst)

def news2(request):
    cookie = request.COOKIES  # cookie是一个字典

    ussername = cookie.get('username')
    counst = {
        'username': ussername
    }
    return render(request,'news2.html',counst)

def news3(request):
    cookie = request.COOKIES  # cookie是一个字典

    ussername = cookie.get('username')
    counst = {
        'username': ussername
    }
    return render(request,'news3.html',counst)

def news4(request):
    cookie = request.COOKIES  # cookie是一个字典

    ussername = cookie.get('username')
    counst = {
        'username': ussername
    }
    return render(request,'news4.html',counst)

def news5(request):
    cookie = request.COOKIES  # cookie是一个字典

    ussername = cookie.get('username')
    counst = {
        'username': ussername
    }
    return render(request,'news5.html',counst)