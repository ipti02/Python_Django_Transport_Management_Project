# yourapp/views.py
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def profile(request):
    students = Student.objects.all()
    return render(request, 'profile.html', {'students': students})
