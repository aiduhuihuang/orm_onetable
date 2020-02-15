from django.http import HttpResponse

def index(request):

    return  HttpResponse("第一个index")
#导包
from django.shortcuts import render
def about(request):
    name="lisi"
    age=20
    params={"name":name,"age":age}
    return  render(request,"index.html",params)