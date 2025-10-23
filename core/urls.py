from django.urls import path
from .views import HomeView, Add_Student, Delete_Student, Edit_Student

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-student/', Add_Student.as_view(), name='add-student'),
    path('delete-student/', Delete_Student.as_view(), name='delete-student'),
    path('edit-student/<int:id>/', Edit_Student.as_view(), name='edit-student')
]