from django.http import HttpResponse
from django.shortcuts import render, redirect
from sagnikapp.models import *
from sagnikapp.bmi.AW import *
from django.contrib import messages
import json
# Create your views here.


def index(request):
   return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        ph = request.POST.get('ph')
        ema = request.POST.get('email')
        messages = request.POST.get('Message')
        contact1 = Contact(name=name, address=address,phone = ph, email = ema,messages= messages)
        contact1.save()
        print(contact1)
    return render(request,"contact.html",request.POST)
    

def bmi(request):
    if request.method == "POST":
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        x = bmi_func(float(height),float(weight))
        y = Health_status(x)
        # bmi1 = BMI(height=height, weight=weight, bmi=diction)
        img1 = Health_statusimg(x)
        # bmi1.save()
        diction = { "img":img1,"bmi":x,"hs":y}
        diction1 = str(x) + " </p><p> "+ y
        messages.success(request, diction1)
        return render(request,"bmi.html",diction)
    else:
        return render(request,"bmi.html")
    
def body_fat(request):
    if request.method == "POST":
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(gender)
        x = bmi_func(float(height),float(weight))
        y = body_fat1(x,int(age),int(gender))
        diction = {"bmi":x,"pr":y}
        messages.success(request, y)
        return render(request,"body_fat.html",diction)
    else:
        return render(request,"body_fat.html")

def calorie(request):
    if request.method == "POST":
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        pa = request.POST.get('pa')
       # x = bmi_func(float(height),float(weight))
       # y = Health_status(x)
        x = calorieaw(int(age),float(weight),float(height),int(pa),int(gender))
        diction = str(x) 
        cal1 = CALORIE(height=height, weight=weight,age=age, gender=gender,physical_activity=pa, calorie=diction)
        cal1.save()
        fat=round(x*28/100,1)
        carbs=round(x*60/100,1)
        protein=round(x*12/100,1)
        data = [fat,carbs,protein]
        context = {'data': data,'fat':fat,'carbs':carbs,'protein':protein}
        messages.success(request, diction)
        return render(request,"calorie.html",context)
    else:
        return render(request,"calorie.html")    

def data(request):
    vari = Contact.objects.all()
    db = {'var':vari}
    print(db)
    return render(request,"data.html",db)

def diet_plan(request):
    x = request.GET.get('cal')
    y = request.POST.get('cal')
    if x:
        z ={"cal":x,"cal":y}
        return render(request,"diet_plan.html",z)
    else:
        return redirect('calorie')
    
def diet_input(request):
    if request.method == "POST":
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        pa = request.POST.get('pa')
        x = calorieaw(int(age),float(weight),float(height),int(pa),int(gender))
        diction = str(x) 
        cal1 = CALORIE(height=height, weight=weight,age=age, gender=gender,physical_activity=pa, calorie=diction)
        cal1.save()
        messages.success(request, diction)
        print(x)
        cal = {"cal":x}
        return render(request,"diet_plan.html",cal)
    else:
        return render(request,"diet_input.html") 

def ideal_weight(request):
    if request.method == "POST":
        h1 = request.POST.get('hf')
        h2 = request.POST.get('hi')
        weight = request.POST.get('weight')
        gender = request.POST.get('gender')
        x = ideal_w(float(h1),float(h2),float(weight),int(gender))
        y = ideal_wmax(float(h1)+(float(h2)/12))
        z = ideal_wmin(float(h1)+(float(h2)/12))
        i = ideal_image(int(gender),float(weight),float(y),float(z))
        diction = {"idw":str(x['dm']),"maxw":str(y),"minw":str(z)}
        diction1 = {"idw":str(x['dm']),"maxw":str(y),"minw":str(z),"img":i,"lg":str(x['lg'])}
        messages.success(request, diction)
        return render(request,"idealw.html",diction1)
    else:
        return render(request,"idealw.html")



def exercise(request):
    return render(request,"exercise.html")

def arm(request):
    return render(request,"arm.html")

def chest(request):
    return render(request,"chest.html")

def leg(request):
    return render(request,"leg.html")

def suryanamaskar(request):
    return render(request,"suryanamaskar.html")

def meditation(request):
    return render(request,"meditation.html")

def detox(request):
    return render(request,"detox.html")

def MuscleGain(request):
    return render(request,"MuscleGain.html")

def Cardio(request):
    return render(request,"Cardio.html")

def loosebellyfat(request):
    return render(request,"loosebellyfat.html")

def beginner(request):
    return render(request,"beginner.html")

def Intermidiate(request):
    return render(request,"Intermidiate.html")

def Advanced(request):
    return render(request,"Advanced.html")




