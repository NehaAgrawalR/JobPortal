from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.


def index(request):
    return render(request,'index.html')

def admin_login(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}        
    return render(request,'admin_login.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')


def user_login(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = SeekerUser.objects.get(user=user)
                if user1.utype == "seeker":
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error':error}
    return render(request,'user_login.html',d)


def user_signup(request):
    error = ""
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        e = request.POST['email']
        p = request.POST['pwd']
        g = request.POST['gender']
        i = request.FILES['image']

        try:
           user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
           SeekerUser.objects.create(user=user,mobile=c,image=i,gender=g,utype="seeker")
           error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'user_signup.html')


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request,'user_home.html')

def Logout(request):
    logout(request)
    return redirect('index')




def provider_login(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = Provider.objects.get(user=user)
                if user1.utype == "provider" and user1.status!="pending":
                    login(request,user)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error':error}
    return render(request,'provider_login.html',d)


def provider_signup(request):
    error = ""
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        com = request.POST['company']
        e = request.POST['email']
        p = request.POST['pwd']
        g = request.POST['gender']
        i = request.FILES['image']

        try:
           user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
           Provider.objects.create(user=user,mobile=c,image=i,gender=g,company=com,utype="provider",status="pending")
           error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'provider_signup.html',d)

def provider_home(request):
    if not request.user.is_authenticated:
        return redirect('provider_login')
    return render(request,'provider_home.html')


def view_user(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = SeekerUser.objects.all()
    d = {'data':data}
    return render(request,'view_user.html',d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    seeker = SeekerUser.objects.get(id=pid)
    seeker.delete()
    return redirect('view_user')


def provider_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Provider.objects.filter(status="pending")
    d = {'data':data}
    return render(request,'provider_pending.html',d)


def provider_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Provider.objects.filter(status="Accept")
    d = {'data':data}
    return render(request,'provider_accepted.html',d)


def provider_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Provider.objects.filter(status="Reject")
    d = {'data':data}
    return render(request,'provider_rejected.html',d)


def provider_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Provider.objects.all()
    d = {'data':data}
    return render(request,'provider_all.html',d)


def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    provider = Provider.objects.get(id=pid)
    if request.method=="POST":
        s = request.POST['status']
        provider.status=s
        try:
            provider.save()
            error="no"
        except:
            error="yes"
    d = {'provider':provider,'error':error}
    return render(request,'change_status.html',d)
    

def delete_provider(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    provider = Provider.objects.get(id=pid)
    provider.delete()
    return redirect('provider_all')


def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passwordadmin.html',d)


def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passworduser.html',d)


def change_passwordprovider(request):
    if not request.user.is_authenticated:
        return redirect('provider_login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passwordprovider.html',d)


def add_job(request):
    if not request.user.is_authenticated:
        return redirect('provider_login')
    error=""
    if request.method=='POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        ds = request.POST['description']
        user = request.user
        provider = Provider.objects.get(user=user)
        try:
           Job.objects.create(provider=provider,start_date=sd,end_date=ed,title=jt,salary=sal,image=l,description=ds,experience=exp,location=loc,skills=skills,creationdate=date.today())
           error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_job.html',d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('provider_login')
    user = request.user
    provider = Provider.objects.get(user=user)
    job = Job.objects.filter(provider=provider)
    d = {'job':job}
    return render(request,'job_list.html',d)


def edit_jobdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('provider_login')
    error=""
    job = Job.objects.get(id=pid)
    if request.method=='POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        ds = request.POST['description']
        user = request.user
        provider = Provider.objects.get(user=user)
        try:
           Job.objects.create(provider=provider,start_date=sd,end_date=ed,title=jt,salary=sal,image=l,description=ds,experience=exp,location=loc,skills=skills,creationdate=date.today())
           error="no"
        except:
            error="yes"
    d = {'error':error,'job':job}
    return render(request,'edit_jobdetail.html',d)


