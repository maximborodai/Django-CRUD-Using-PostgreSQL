from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Student
from .models import Teacher

from .forms import StudentForm

import pandas as pd


headers = {'First_Name':'asc',
         'Last_Name':'asc',
         'Date_Of_Birth':'asc',}

'''
def table_view(request):
    sort = request.GET.get('sort')
    records = Record.objects.all()

    if sort is not None:
        records = records.order_by(sort)

        if headers[sort] == "des":
            records = records.reverse()
            headers[sort] = "asc"
        else:
            headers[sort] = "des"
    
    context = {'user':request.user,'profile':request.user.get_profile(),'records':records}  
    return render_to_response("Index.html", context)
'''

# Create your views here.
def Add_Student_Info(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        context = {'has_error': False}
        Admission_Number = request.POST.get('Admission_Number')
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Date_Of_Birth = request.POST.get('Date_Of_Birth')
        Date_Joined = request.POST.get('Date_Joined')
        Faculty = request.POST.get('Faculty')
        Department = request.POST.get('Department')
        Year_Of_Study = request.POST.get('Year_Of_Study')
        Unit_Name = request.POST.get('Unit_Name')
        Grade = request.POST.get('Grade')

        student = Student.objects.create(Admission_Number=Admission_Number, First_Name=First_Name, Last_Name=Last_Name,
        Date_Of_Birth=Date_Of_Birth, Date_Joined=Date_Joined, Faculty=Faculty, Department=Department,
        Year_Of_Study=Year_Of_Study, Unit_Name=Unit_Name, Grade=Grade).save()

        if not context['has_error']:
            messages.success(request, '✅ Student Info Successfully Added!')
            return redirect('Add_Student_Info')
        
        else:
            messages.error(request, '⚠️ Student Info Unsuccessfully Added!')
            return redirect('Add_Student_Info')
    
    # sorting teachers----------
    sort = request.GET.get('sort')
    #records = Teacher.objects.all()

    if sort is not None:
        teachers = teachers.order_by(sort)

        if headers[sort] == "des":
            teachers = teachers.reverse()
            headers[sort] = "asc"
        else:
            headers[sort] = "des"

    context = {'students': students, 'form': form, 'teachers': teachers}
    
    return render(request, 'Index.html', context)

def View_Student_Info(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
    else:
        form = StudentForm(instance=student)

    context = {'student': student, 'form':form}
    return render(request, 'View.html', context)

def Edit_Student_Info(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Student Info Successfully Updated!')
            return redirect('Add_Student_Info')
        else:
            messages.error(request, '⚠️ Student Info Unsuccessfully Updated!')
            return redirect('Add_Student_Info')
    else:
        form = StudentForm(instance=student)
    
    context = {'student':student, 'form':form} 
    return render(request, 'Edit.html', context)
    

def Delete_Student_Info(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('Add_Student_Info')

'''
def View_Teacher_Info(request, id):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
    else:
        form = StudentForm(instance=student)

    context = {'student': student, 'form':form}
    return render(request, 'View.html', context)

def Add_Teacher_Info(request):
    teachers = Teacher.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        context = {'has_error': False}
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Date_Of_Birth = request.POST.get('Date_Of_Birth')
        Faculty = request.POST.get('Faculty')
        Department = request.POST.get('Department')
        #Grade = request.POST.get('Grade')

        teacher = Teacher.objects.create(First_Name=First_Name, Last_Name=Last_Name,
        Date_Of_Birth=Date_Of_Birth, Faculty=Faculty, Department=Department).save()

        if not context['has_error']:
            messages.success(request, '✅ Teacher Info Successfully Added!')
            return redirect('Add_Teacher_Info')
        
        else:
            messages.error(request, '⚠️ Teacher Info Unsuccessfully Added!')
            return redirect('Add_Teacher_Info')
    
    context = {'teachers': teachers, 'form': form}  
    return render(request, 'Index.html', context)
    '''

# TO-FIX: Отгружает несортированный список
def Teacher_Info_To_Excel(request):
    list1, list2, list3, list4, list5 = [], [], [], [], []

    col1, col2, col3, col4, col5 = "First_Name", "Last_Name", "Date_Of_Birth", "Faculty", "Department"

    teachers = Teacher.objects.all()

    sort = request.GET.get('sort')    

    if sort is not None:
        teachers = teachers.order_by(sort)

        if headers[sort] == "des":
            teachers = teachers.reverse()
            headers[sort] = "asc"
        else:
            headers[sort] = "des"

    list1 = [teacher.First_Name for teacher in teachers]
    list2 = [teacher.Last_Name for teacher in teachers]
    list3 = [teacher.Date_Of_Birth for teacher in teachers]
    list4 = [teacher.Faculty for teacher in teachers]
    list5 = [teacher.Department for teacher in teachers]

    data = pd.DataFrame({col1:list1, col2:list2, col3:list3, col4:list4, col5:list5})

    data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)
    messages.success(request, '✅ Teachers Info Successfully Written to Excel!')

    #context = {'teachers': teachers}
    return redirect('Add_Student_Info')
