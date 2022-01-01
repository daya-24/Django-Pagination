from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.studentview, name='show_stud'),
    path('add/', views.addView, name='add_stud'),
    path('delete/<int:i>/', views.delete, name='delete'),
    path('update/<int:i>/', views.update, name='update')
]