from django.shortcuts import render, redirect
from studentrecords.forms import StudentForm
from studentrecords.models import Students
# Create your views here.
app_name = 'first_app'

def index(request):
    return render(request,'base.html')
def searchpage(request):
    return render(request,'search.html')
def stud(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/show')
    else:
        form = StudentForm()
    return render(request,'index.html',{'form':form})
def search(request):
    if request.method == 'POST':
        try:
           Reg_no = request.POST['Reg_no']
           student = Students.objects.get(Reg_no=Reg_no)
           return render(request,"shows.html",{'student':student})
        except:
           return render(request,"shows.html",{'insertme':"Student with the entered register number does not Exist."})
def show(request):
    students = Students.objects.all()
    return render(request,"show.html",{'students':students})
def edit(request, Reg_no):
    student = Students.objects.get(Reg_no=Reg_no)
    return render(request,'edit.html', {'student':student})
def update(request, Reg_no):
    student = Students.objects.get(Reg_no=Reg_no)
    form = StudentForm(request.POST, instance = student)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'student': student})
def destroy(request, Reg_no):
    student = Students.objects.get(Reg_no=Reg_no)
    student.delete()
    return redirect("/show")
