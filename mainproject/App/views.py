from django.shortcuts import redirect, render
from App.models import*

# Create your views here.

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        print(name)
        print(age)
        Student.objects.create(
            name=name,
            age=age

    )
    queryset =Student.objects.all()
    context ={'form':queryset}
    return render(request,"form.html",context)

def delete_Student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect ('table')

def header(request):
    queryset=Student.objects.all()
    context={'form':queryset}
    return render(request,"form.html",context)    

def update(request,id):
    queryset=Student.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        print(name)
        print(age)
        Student.objects.filter(id=id).update(
            name=name,
            age=age
    
    )
        return redirect('table')
    queryset=Student.objects.all()
    context={'form':queryset}
    return render(request,"update.html",context)


def table(request):

    queryset =Student.objects.all()
    context ={'form':queryset}
    return render(request,"table.html",context)

def project(request):
    return render(request,"project1.html",)  

def header2(request):
    queryset=Student.objects.all()
    context={'form':queryset}
    return render(request,"header2.html",context) 


def project2(request):
    hello=Data.objects.all()
    context={'data':hello}
    return render(request,"project2.html",context)


def dashboard(request):
    hello=Data.objects.all()
    context={'data':hello}
    return render(request,"dashboard.html",context)






def detail(request):
    if request.method == "POST":
        name = request.POST.get("name")
        prize = request.POST.get("prize")
        image = request.FILES.get("image")

        Data.objects.create(
            name=name,
            prize=prize,
            image=image,
        )
        return redirect('dashboard')
    hello=Data.objects.all()
    context={'data':hello}
    return render(request, "detail.html",context)


def delete_data(request, id):
    item =Data.objects.get( id=id)
    item.delete()
    return redirect('dashboard')


def update2(request,id):
    queryset=Data.objects.get(id=id)
    if request.method == "POST":
        name=request.POST.get("name")
        prize=request.POST.get("prize")
        if  request.FILES.get("image"):
            image = request.FILES.get("image")
        print(name)
        print(prize)
        print(image)

        Data.objects.filter(id=id).update(
             name=name,
             prize=prize,
             image=image,
    
    )
        return redirect('dashboard')
    queryset=Data.objects.all()
    context={'detail':queryset}
    return render(request,"update2.html",context)

    




  

   
    

