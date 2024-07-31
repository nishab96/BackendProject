from django.urls import path
 
from . import views
 
urlpatterns = [

    path('add_post/',views.add_post),
    path('delete_post/<int:id>/',views.delete_post),
    path('update_post/<int:id>/',views.update_post),
    path('read_post/<int:id>',views.read_post),
    path('read_post_all/',views.read_post_all),
    path('add-student/', views.add_student, name='add_student'),
    path('get-student/<int:student_id>/', views.get_student_by_id, name='get_student_by_id'),
    path('get-all-students/', views.get_all_students, name='get_all_students'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('update-student/<int:student_id>/', views.update_student, name='update_student'),
    path('add_school', views.school, name='add_school'),
    path('delete-student/', views.delete_student, name='delete_student'),
    path('login', views.login, name='login'),


]