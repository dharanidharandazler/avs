# avs_attendance_app/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from avs_attendance_app_BA_eco import models
from .forms import StudentForm
from .models import Student
from django.urls import reverse


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'avs_attendance_app_BA_eco/add_student.html', {'form': form})



def student_list(request):
    students = Student.objects.all()
    return render(request, 'avs_attendance_app_BA_eco/student_list.html', {'students': students})



def save_attendance(request):
    if request.method == 'POST':
        total_students = Student.objects.count()
        present_students = 0

        for student in Student.objects.all():
            attendance_status = request.POST.get(f'attendance_{student.id}', None)
            if attendance_status == 'present':
                student.present = True
                student.absent = False
                present_students += 1
            elif attendance_status == 'absent':
                student.present = False
                student.absent = True
            else:
                student.present = False
                student.absent = False

            student.save()

        total_percentage = (present_students / total_students) * 100

        # Use reverse() to get the URL for the 'absent_list' view
        return redirect(reverse('absent_list', kwargs={'total_percentage': total_percentage}))
    
    return HttpResponse("Invalid request method")

def absent_list(request, total_percentage):
    total_percentage = float(total_percentage)

    # Filter students based on the 'absent' field
    absent_students = Student.objects.filter(absent=True)

    context = {'absent_students': absent_students, 'total_percentage': total_percentage}
    return render(request, 'absent_list.html', context)
    
