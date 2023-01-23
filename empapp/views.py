from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import details
import faker
fake = faker.Faker()

# Create your views here.

def gettingdata(request):
    for i in range(100):
        details(
        Firstname = fake.first_name(),
        Lastname = fake.last_name(),
        Email = fake.email(),
        Company = fake.random_element(elements = ('INFOSYS','TCS','CTC','WIPRO')),
        Location = fake.random_element(elements = ('hyd','bang','pune','chenai')),
        Salary = fake.random_element(elements = (20000,30000,25000,35000)),
        Address = fake.address()
        ).save()
    return HttpResponse('data saved successfully')
def show(request):
    data = details.objects.all()
    return render( request,'table.html',{'data':data})
def Hyderabad(request):
    if request.method == 'GET':   
        emps = details.objects.filter(Location = 'hyd')
        return render( request,'Hyderabad.html',{'emps':emps})
    else:
        com = request.POST['data']
        emps = details.objects.filter(Location='hyd') & details.objects.filter(Company=com)
        return render( request,'Hyderabad.html',{'emps':emps})
        
def Banglore(request):
    if request.method == 'GET':   
        emps = details.objects.filter(Location = 'bang')
        return render( request,'Banglore.html',{'emps':emps})
    else:
        com = request.POST['data']
        emps = details.objects.filter(Location='bang') & details.objects.filter(Company=com)
        return render( request,'Banglore.html',{'emps':emps})
def Chennai(request):
    if request.method == 'GET':   
        emps = details.objects.filter(Location = 'chenai')
        return render( request,'Chennai.html',{'emps':emps})
    else:
        com = request.POST['data']
        emps = details.objects.filter(Location='chenai') & details.objects.filter(Company=com)
        return render( request,'Chennai.html',{'emps':emps})
def Pune(request):
    if request.method == 'GET':   
        emps = details.objects.filter(Location = 'pune')
        return render( request,'Pune.html',{'emps':emps})
    else:
        com = request.POST['data']
        emps = details.objects.filter(Location='pune') & details.objects.filter(Company=com)
        return render( request,'Pune.html',{'emps':emps})
def Homepage(request):
    return render( request,'Homepage.html')

