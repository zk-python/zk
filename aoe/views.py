from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print('第一个视图函数')
    return HttpResponse('呵呵呵')

def login(requst):
    print('第二个视图函数')
    return HttpResponse('heiheihie')

def book(request):
    print('这是第三个视图函数')
    return HttpResponse('去问问请问的')