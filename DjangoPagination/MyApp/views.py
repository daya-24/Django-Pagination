from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator

def studentview(request):
    student = Student.objects.all()
    paginator = Paginator(student, 3)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    return render(request, 'MyApp/show_stud.html', {'page_obj': page_obj})

def addView(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            rollno = form.cleaned_data['rollno']
            name = form.cleaned_data['name']
            standard = form.cleaned_data['standard']
            stream = form.cleaned_data['stream']
            city = form.cleaned_data['city']

            s1 = Student(rollno=rollno, name=name, standard=standard, stream=stream, city=city)
            s1 .save()
            return redirect('add_stud')
    template_name = 'MYApp/add_stud.html'
    context = {'form': form}
    return render(request, template_name, context)

def delete(request,i):
    student = Student.objects.get(id=i)
    student.delete()
    return redirect('show_stud')

def update(request,i):
    student=Student.objects.get(id=i)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('show_stud')
    template_name = 'MyApp/add_stud.html'
    context = {'form': form}
    return render(request, template_name, context)