from django.shortcuts import render,redirect
from .import forms
from .import models
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.db import connection, transaction
from . import models
import json
from django.core import serializers

# Create your views here.

def home(request):
    username = request.session['username']
    id=''
    user=''
    email=''
    mobile=''
    adhaar=''
    percentage=''
    user = models.DpyTable.objects.all().filter(username__iexact=username)
    data = serializers.serialize( "python", models.DpyTable.objects.all().filter(username__iexact=username) )
    count=0
    for detail in user :
        id = detail.id
        username = detail.username
        email = detail.email
        mobile = detail.mobile_number
        adhaar = detail.adhaar_number
        if email == "None" or email == None:
         count=count+1

        if mobile == "None" or email == None:
         count=count+1

        if adhaar == "None" or email == None:
         count=count+1

        percentage = (5-count)/5 * 100;
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM dpy_table where username=%s ",[username])
    # results = cursor.fetchone()
    # email = result[0]
    # mobile = result[1]
    # adhaar = result[2]'userdata':userdata
    return render(request,'home.html',{'data':data,'count':percentage , 'id':id})

def login(request):
    form = forms.User_form()
    return render(request,'registration/Login.html',{'form':form})

def signup(request):
    form = forms.User_form()
    return render(request ,'SignUp.html',{'form':form})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': models.DpyTable.objects.all().filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def update_user(request):
    data = request.POST.getlist('studentData[]')
    models.DpyTable.objects.filter(id=data[0]).update(email=data[3],mobile_number=data[4],adhaar_number=data[5])
    response_data ={'Status':True, 'Message':'Successfully Updated.'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def insert_user(request):
    usern = request.POST.get('username', None)
    passwd = request.POST.get('password', None)
    u = models.DpyTable(username=usern,password=passwd)
    u.save()
    response_data ={'Status':True, 'Message':'successfully Added.'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def validate_login(request):
    if request.method=='GET':
        loginData = request.GET.getlist('loginData[]')
        username = loginData[0]
        password = loginData[1]
        cursor = connection.cursor()
        cursor.execute("SELECT password FROM dpy_table where username=%s",[username])
        result = cursor.fetchone()
        actualpass = result[0]
        if password==actualpass:
            response_data ={'Status':True, 'Message':'Login Successfull.'}
            request.session['username'] =username
            return redirect('dpyApp:home')
        else:
            response_data ={'Status':False, 'Message':'Wrong Login data.'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")

def logout(request):
    del request.session['username']
    return redirect("dpy_acounts:login_user")