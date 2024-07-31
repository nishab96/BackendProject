from django.db import models

# Create your models here.
 
class newApp(models.Model):
    id =  models.BigAutoField(auto_created=True, primary_key=True)
    first_name = models.CharField(max_length=30 , null=True)
    last_name = models.CharField(max_length=30 ,null=True)
    current_password = models.CharField(max_length=100 ,null=True)
    #new_password = models.CharField(max_length=100 ,null=True)
    email = models.EmailField(max_length=254 ,null=True)
    phone_number = models.CharField(max_length=20 ,null=True)
    state = models.CharField(max_length=50 ,null=True)
    gender = models.CharField(max_length=1, null=True )
    date_of_birth = models.DateField()
    role=models.CharField(max_length=20 ,default="user")
 
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

class School(models.Model):
    school_id = models.BigAutoField(auto_created=True, primary_key=True)
    school_name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)

def __str__(self):
        return self.school_name


class Student(models.Model):
    stud_id = models.BigAutoField(auto_created=True, primary_key=True)
    stud_fname = models.CharField(max_length=30, null=True)
    stud_lname = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, null=True)
    dob = models.DateField()
    state = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1, null=True)
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

def __str__(self):
        return f"{self.stud_fname} {self.stud_lname}"





