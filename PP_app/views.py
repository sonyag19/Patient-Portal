import os

from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def Navbar(request):
    return render(request,'Navbar.html')

def Footer(request):
    return render(request,'footer.html')

def Index(request):
    return render(request,'index.html')

# def SignUp(request):
#     if request.method=='POST':
#         a=SignUpForm(request.POST)
#         if a.is_valid():
#             fnm=a.cleaned_data['fname']
#             lnm=a.cleaned_data['lname']
#             ge = a.cleaned_data['gender']
#             em=a.cleaned_data['email']
#             ps=a.cleaned_data['password']
#             cp=a.cleaned_data['cpassword']
#             # dr=a.cleaned_data['doctor']
#             dte=a.cleaned_data['date']
#             mth=a.cleaned_data['month']
#             yr=a.cleaned_data['year']
#             ad1=a.cleaned_data['addr1']
#             ad2=a.cleaned_data['addr2']
#             cty=a.cleaned_data['city']
#             ctry=a.cleaned_data['country']
#             zp=a.cleaned_data['zip']
#             ph = a.cleaned_data['phone']
#             pt=a.cleaned_data['photo']
#             if ps==cp:
#                 b=SignUpModel(fname=fnm,lname=lnm,gender=ge,email=em,password=ps,
#                               # doctor=dr,
#                               date=dte,month=mth,year=yr,addr1=ad1,addr2=ad2,
#                               city=cty,country=ctry,zip=zp,phone=ph,photo=pt)
#                 b.save()
#                 return HttpResponse("Registration Success")
#             else:
#                 return HttpResponse("Password doesn't match")
#         else:
#             return HttpResponse("Registration Failed")
#     else:
#         return render(request,'SignUp.html')


class SignUp(generic.CreateView):
    form_class=SignUpForm
    template_name='SignUp.html'
    success_url= reverse_lazy('login')

# def Login(request):
#     if request.method=='POST':
#         a=SignUpForm(request.POST)
#         if a.is_valid():
#             em=a.cleaned_data['email']
#             ps=a.cleaned_data['password']
#             b=SignUpModel.objects.all()
#             for i in b:
#                 if em==i.email and ps==i.password:
#                     # email=i.email
#                     return HttpResponse("Login Success")
#             else:
#                 return HttpResponse("Login failed")
#     else:
#         return render(request,'Login.html')

class Login(generic.View):
    form_class=Loginform
    template_name='Login.html'
    def get(self,request):
        form=self.form_class
        return render(request,'Login.html',{'form':form})

    def post(self,request):
        if request.method =='POST':
            a=Loginform(request.POST)
            if a.is_valid():
                em=a.cleaned_data['email']
                ps=a.cleaned_data['password']
                b=SignUpModel.objects.all()
                for i in b:
                    if em==i.email and ps==i.password:
                        return HttpResponse("login success")
                        # success= reverse_lazy('home')

                else:
                    return HttpResponse("login failed")

def Profile(request):
    pro=SignUpModel.objects.all()
    for i in pro:
        id1=i.id
        fn=i.fname
        ln=i.lname
        ph=i.phone
        em=i.email
        ad1=i.addr1
        ad2=i.addr2
        cy=i.city
        cty=i.country
        zp=i.zip
        dte=i.date
        pht=i.photo
        return render(request,'Profile.html',{'id':id1,'fname':fn,'lname':ln,'phone':ph,'email':em,'addr1':ad1,'addr2':ad2,'city':cy,'country':cty,'zip':zp,'date':dte,'photo':pht})


def edit_profile(request,id):
    prod=SignUpModel.objects.get(id=id)
    li=str(prod.photo).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES) !=0:
            if len(prod.photo) > 0:
                os.remove(prod.photo.path)
            prod.photo=request.FILES['photo']
        prod.fname=request.POST.get('fname')
        prod.lname = request.POST.get('lname')
        prod.phone=request.POST.get('phone')
        prod.email=request.POST.get('email')
        prod.addr1=request.POST.get('addr1')
        prod.addr2 = request.POST.get('addr2')
        prod.city = request.POST.get('city')
        prod.country = request.POST.get('country')
        prod.zip = request.POST.get('zip')
        prod.save()
        return redirect(Profile)
    context={'prod':prod,'li':li}
    return render(request,'edit_profile.html',context)

def LoginAll(request):
    return render(request,'LoginAll.html')


def home(request,id):
    a = SignUpModel.objects.get(id=id)
    if request.method=='POST':
        a.id=request.POST.get('id')
        a.email=request.POST.get('email')
        a.fname=request.POST.get('fname')
        a.save()
        return redirect(home)
    return render(request,'home.html',{'a':a})


# def new_Appointment(request):
#     return render(request,'NewAppointment.html')

class newApptClass(generic.CreateView):
    form_class=NewAppointmentForm
    template_name='NewAppointment.html'
    success_url= reverse_lazy('visits')

def visits(request):
    return render(request,'visits.html')
    # a=newAppointment.objects.all()
    # for i in a:
    #     id1=i.id
    #     adate=i.apptDate
    #     atime=i.apptTime
    #     dr=i.doctor
    #     ad=i.appointment_description
    #     return render(request,'visits.html',{'id':id1,'apptDate':adate,'apptTime':atime,'doctor':dr,'appointment_description':ad})

