from django.urls import path
from StudentRegister import views

urlpatterns = [
    path('',views.Add_Student_Info, name='Add_Student_Info'),
    #path('',views.Add_Teacher_Info, name='Add_Teacher_Info'),
    path('delete/<int:id>',views.Delete_Student_Info, name='Delete_Student_Info'),
    path('view/<int:id>',views.View_Student_Info, name='View_Student_Info'),
    path('edit/<int:id>',views.Edit_Student_Info, name='Edit_Student_Info'),
    path('to_excel',views.Teacher_Info_To_Excel, name='Teacher_Info_To_Excel'),
]