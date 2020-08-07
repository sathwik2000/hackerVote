from django.shortcuts import render,redirect
from rest_framework.views import APIView,View
from rest_framework.parsers import JSONParser
from .serializers import HackerSerializer
from django.views.decorators.csrf import csrf_exempt
from vote.models import Hacker
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

admin1 = "123456"  #my admin password

class hackers(APIView):
    @csrf_exempt
    def post(self,request):
        data = JSONParser().parse(request)
        password = data["password"]
        data.pop('password', None)
        serializer = HackerSerializer(data=data)
        print(password,admin1)
        if password != admin1:
            if serializer.is_valid():
                return JsonResponse(serializer.errors, status=401)
        else:
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse(serializer.errors, status=400)

    def put(self,request,hacker,password):
        ha=""
        try:
            ha = Hacker.objects.get(code=password)
            #print(ha.Name,hacker)
        except:
            k =0
        if (password != admin1) and (ha.Name != hacker):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            hack = Hacker.objects.get(Name=hacker)
        except Hacker.DoesNotExist:
            return JsonResponse(serializer.errors, status=404)
        data = JSONParser().parse(request)
        serializer = HackerSerializer(hack,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    def delete(self,request,hacker,password):
        if password != admin1:
            return JsonResponse(serializer.errors, status=401)
        hack = Hacker.objects.get(Name=hacker)
        hack.delete()
        return Response(status=status.HTTP_200_OK)
    

def hack(request,name):
    hack = Hacker.objects.get(Name=name)
    data = {}
    if "vote" in request.COOKIES:
        vo = request.COOKIES['vote']
        print(vo)
        if vo == "done":
            data['vote'] = False
        else:
            data['vote'] = True
    else:
        data['vote'] = True
    data['user'] = hack
    return render(request,"home.html",data)

def all(request):
    hack = Hacker.objects.all()
    #print(hack)
    data = {}
    data['hackers'] = hack
    return render(request,"main.html",data)
    
def vote(request,name):
    hack = Hacker.objects.get(Name=name)
    try:
        vo = request.COOKIES['vote']
        if vo == "done":
            return HttpResponse("already voted")
        else:
            hack = Hacker.objects.get(Name=name)
            data = {}
            data['hackers'] = hack
            response = HttpResponse("voted")
            hack.votes += 1
            response.set_cookie('vote', 'done')
            return response
    except:
        hack = Hacker.objects.get(Name=name)
        data = {}
        data['hackers'] = hack
        response = HttpResponse("voted")
        hack.votes += 1
        response.set_cookie('vote', 'done')
        return response

def admin(request):
    if request.method == "GET":
        return render(request,"admin.html")
    if request.method == "POST":
        password = request.POST.get("password")
        #print(password)
        if password == "123456":
            data = {}
            hack = Hacker.objects.all()
            data["who"] = "admin"
            request.session['who'] = "admin"
            data["hackers"] = hack
            return render(request,"land.html",data)

def candidate(request):
    if request.method == "GET":
        return render(request,"candidate.html")
    if request.method == "POST":
        password = request.POST.get("password")
        hack = Hacker.objects.filter(code=password).exists()
        if hack:
            data = {}
            hack = Hacker.objects.all()
            hack1 = Hacker.objects.get(code=password)
            request.session['who'] = hack1.Name
            data["hackers"] = hack
            return render(request,"land.html",data)
    
def user(request):
    hack = Hacker.objects.all()
    #print(hack)
    data = {}
    data["who"] = "user"
    request.session['who'] = "user"
    data['hackers'] = hack
    return render(request,"land.html",data)
