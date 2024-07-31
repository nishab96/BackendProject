from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import newApp
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from .models import Student, School


# from newApp.models import Posts, newApp
# Create your views here.
 
@csrf_exempt
def add_post(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        # employee_id = request.POST.get('id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        current_password = data.get('current_password')
        #new_password = data.get('new_password')
        email = data.get('email')
        phone_number = data.get('phone_number')
        state = data.get('state')
        date_of_birth = data.get('date_of_birth')
        role = data.get('role')
       
        newApp.objects.create(
            # employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            current_password=current_password,
            #new_password=new_password,
            email=email,
            phone_number=phone_number,
            state=state,
            date_of_birth=date_of_birth,
            role=role
        )
    return JsonResponse({'message': 'Profile created successfully'}, status=201)
   
#delete  
@csrf_exempt  
def delete_post(request, id):
    if request.method=='DELETE':
        Id=id
        if newApp.objects.filter(id=Id).count()>0:
            userdata=newApp.objects.get(id=id)
            userdata.delete()
            return JsonResponse("data deleted", safe=False)
        return JsonResponse("data not found", safe=False)
    else:
        return JsonResponse("delete method required", safe=False)
 
#update
@csrf_exempt
def update_post(request, id):
    data=json.loads(request.body)
    if request.method=='PUT':
        Id=id
        if newApp.objects.filter(id=Id).count()>0:
            userdata=newApp.objects.get(id=id)
            userdata.first_name=data.get('first_name')
            userdata.last_name=data.get('last_name')
            userdata.current_password=data.get('current_password')
            userdata.new_password=data.get('new_password')
            userdata.email=data.get('email')
            userdata.phone_number=data.get('phone_number')
            userdata.state=data.get('state')
            userdata.gender=data.get('gender')
            userdata.date_of_birth=data.get('date_of_birth')
            userdata.save()
    return JsonResponse({'message': 'Data Updated successfully'}, status=200)
   

    # return JsonResponse({'message': 'Profile updated successfully'}, status=201)

#get filed by id
@csrf_exempt
def read_post(request,id):
    if request.method == 'GET':
        profile = newApp.objects.get(id=id)
        data=[]
        data.append({
                'id': profile.id,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'current_password': profile.current_password,
                'new_password': profile.new_password,
                'email': profile.email,
                'phone_number': profile.phone_number,
                'state': profile.state,
                'gender': profile.gender,
                'date_of_birth': profile.date_of_birth
            })
        return JsonResponse(data, safe=False)
 
# get all fields 
@csrf_exempt
def read_post_all(request):
    if request.method == 'GET':
        profiles = newApp.objects.all()
        data = []
        for profile in profiles:
            data.append({
                'id': profile.id,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'current_password': profile.current_password,
                'new_password': profile.new_password,
                'email': profile.email,
                'phone_number': profile.phone_number,
                'state': profile.state,
                'gender': profile.gender,
                'date_of_birth': profile.date_of_birth
            })
        return JsonResponse(data, safe=False)
 

#Students and School
#post
@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode("utf-8"))
            stud_fname = data.get('stud_fname')
            stud_lname = data.get('stud_lname')
            city = data.get('city')
            email = data.get('email')
            dob = data.get('dob')
            state = data.get('state')
            gender = data.get('gender')
            school_id = data.get('school_id')
            
            if not all([stud_fname, stud_lname, city, email, dob, state, gender, school_id]):
                return JsonResponse({'error': 'Missing fields in request'}, status=400)
            
            school = get_object_or_404(School, pk=school_id)
            student = Student.objects.create(
                stud_fname=stud_fname,
                stud_lname=stud_lname,
                city=city,
                email=email,
                dob=dob,
                state=state,
                gender=gender,
                school=school

            )
            return JsonResponse({'message': 'Student created successfully'}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def school(request):
    if request.method == "POST":
        try: 
            data=json.loads(request.body)
            school_name_var = data.get('school_name')
            address_var = data.get('address')

            school = School.objects.create(
                school_name=school_name_var,
                address = address_var
            )
        except:
             return JsonResponse({'error': 'there is some issue while creating school'}, status=400)
      
    return JsonResponse({'message': 'school created successfully'}, status=201)

    
#get studentsby Id
@csrf_exempt
def get_student_by_id(request, student_id):
    if request.method == 'GET':
        try:
            student = Student.objects.get(stud_id=student_id)
            student_data = {
                'stud_id': student.stud_id,
                'stud_fname': student.stud_fname,
                'stud_lname': student.stud_lname,
                'city': student.city,
                'email': student.email,
                'dob': student.dob,
                'state': student.state,
                'gender': student.gender,
                'school': student.school.school_name
            }
            return JsonResponse(student_data, status=200)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
    else:
        return JsonResponse({'error': 'GET method required'}, status=405)

#get all students
@csrf_exempt
def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        student_data = list(students.values())
        return JsonResponse(student_data, safe=False, status=200)
    else:
        return JsonResponse({'error': 'GET method required'}, status=405)
    
#delete
@csrf_exempt
def delete_student(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        try:
               
            stud_id = data["stud_id"]
            user_id=data["user_id"]

            user=newApp.objects.filter(id=user_id).values().get()

            if user["role"] == "admin":
                student=list(Student.objects.filter(stud_id=stud_id).values().get())

                if len(student)!=0:
                    delete_student=Student.objects.get(stud_id=stud_id)
                    delete_student.delete()
                    return JsonResponse({'message': 'Student deleted successfully'}, status=200)
                else:
                    return JsonResponse({'error': 'Student not found or unable to delete'}, status=404)
            
            return JsonResponse({'message': 'Student deleted successfully'}, status=200)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
    else:
        return JsonResponse({'error': 'DELETE method required'}, status=405)
    
#update 
@csrf_exempt
def update_student(request, student_id):
    if request.method == 'PUT':
        try:
            student = Student.objects.get(stud_id=student_id)
            data = json.loads(request.body)
            student.stud_fname = data.get('stud_fname', student.stud_fname)
            student.stud_lname = data.get('stud_lname', student.stud_lname)
            student.city = data.get('city', student.city)
            student.email = data.get('email', student.email)
            student.dob = data.get('dob', student.dob)
            student.state = data.get('state', student.state)
            student.gender = data.get('gender', student.gender)
            student.save()
            return JsonResponse({'message': 'Student updated successfully'}, status=200)
        except Student.DoesNotExist: data=json.loads(request.body)
        return JsonResponse({'error': 'Student not found'}, status=404)
    else:
        return JsonResponse({'error': 'PUT method required'}, status=405)



@csrf_exempt
def login(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        try:
            email = data['email']
            current_password = data['current_password']
            student_email=data['student_email']
 
            user=newApp.objects.filter(email=email).values().get()
 
            if newApp.objects.filter(email=email):
                if user["role"] == "admin":
                    student=list(Student.objects.filter(student_email=student_email).values())
 
                    if len(student)!=0:
                        delete_student=Student.objects.get(student_email=student_email)
                        delete_student.delete()
                        return JsonResponse({'message': 'Student deleted successfully'}, status=200)
                    else:
                        return JsonResponse({'error': 'Student not found or unable to delete'}, status=404)
                   
                elif user["role"] == "user":
                    student=list(Student.objects.filter(student_email=student_email).values())
                    if len(student)!=0:
                        student_details=Student.objects.get(student_email=student_email)
                        student_details = vars(Student)
                        return JsonResponse({'student_details': student_details}, status=200)
                    else:
                        return JsonResponse({'error': 'Student not found or unable to delete'}, status=404)
                    
 
                return JsonResponse({'message': 'Only admin has rights to delete'})
       
            return JsonResponse({'message': 'user dose not exist'})
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)