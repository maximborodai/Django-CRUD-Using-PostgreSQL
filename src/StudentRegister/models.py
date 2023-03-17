from django.db import models

# Create your models here.
class Student(models.Model):
    Admission_Number = models.CharField(max_length=50, verbose_name='Admission Number', null=True)
    First_Name = models.CharField(max_length=50, verbose_name='First Name',null=True)
    Last_Name = models.CharField(max_length=50, verbose_name='Last Name',null=True)
    Date_Of_Birth = models.DateField(max_length=50, verbose_name='Date Of Birth', null=True)
    Date_Joined = models.DateField(verbose_name='Date Joined', null=True)
    Faculty = models.CharField(max_length=50, verbose_name='Faculty', null=True)
    Department = models.CharField(max_length=50, verbose_name='Department',null=True)
    #Course_Name = models.CharField(max_length=50, verbose_name='Course Name')
    Year_Of_Study = models.CharField(max_length=50, verbose_name='Year of Study',null=True)
    Unit_Name = models.CharField(max_length=50, verbose_name='Unit Name',null=True)
    Grade = models.CharField(max_length=50, verbose_name='Grade',null=True)

    def __str__(self):
        return self.Admission_Number


class Teacher(models.Model):
    First_Name = models.CharField(max_length=50, verbose_name='First Name', null=True)
    Last_Name = models.CharField(max_length=50, verbose_name='Last Name', null=True)
    Date_Of_Birth = models.DateField(max_length=50, verbose_name='Date Of Birth', null=True)
    Faculty = models.CharField(max_length=50, verbose_name='Faculty', null=True)
    Department = models.CharField(max_length=50, verbose_name='Department', null=True)

'''
    def __str__(self):
        return self.Last_Name
'''

'''
class Course(models.Model):
    Course_Name = models.CharField(max_length=50, verbose_name='First Name', null=True)
    Teacher_id = models.CharField(max_length=50, verbose_name='Last Name', null=True)
    Student_id = models.DateField(max_length=50, verbose_name='Date Of Birth', null=True)
    Faculty = models.CharField(max_length=50, verbose_name='Faculty', null=True)
    Department = models.CharField(max_length=50, verbose_name='Department', null=True)


    def __str__(self):
        return self.Course_Name
'''
    # SELECT generate_series(1,10) AS id, md5(random()::text) AS descr;
    