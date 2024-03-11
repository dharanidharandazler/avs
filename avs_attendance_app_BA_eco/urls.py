
from django.urls import path
from avs_attendance_app_BA_eco import views



urlpatterns = [
    path('', views.add_student,name='add_student'),
    path('student_list/', views.student_list,name='student_list'),
    path('save_attendance/', views.save_attendance,name='save_attendance'),
    path('absent_list/<str:total_percentage>/', views.absent_list,name='absent_list'),
    path('absent_list/', views.absent_list, name='absent_list')
    
]
