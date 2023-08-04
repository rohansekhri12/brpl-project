# my creation!!
from django.http import HttpResponse 
from django.shortcuts import render
def home(request):
    dic={'name':'yash','surname':'sharma'}
    return render(request,'test.html',dic)
def index(request):
    f=open("data.txt","r")
    return HttpResponse(f.readlines())

""" def wp(request):
    return HttpResponse('''<a href="https://web.whatsapp.com/">Whatsapp</a>''')

def about(request):
    return HttpResponse(''' <a href="http://127.0.0.1:8000/">HOME</a>''')
def yt(request):
    return HttpResponse('''<a href="https://www.youtube.com/watch?v=HdoPg2e_m9s&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=2&ab_channel=CodeWithHarry">Youtube</a>''')

     """