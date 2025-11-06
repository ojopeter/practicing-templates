from django.shortcuts import render

# Create your views here.
def home(request):
    stats = {
        "courses": 4,
        "completed": 3,
        "cgpa": 4.14

    }
    
    comp = True if stats['completed'] >=3 else False
    return render(request, 'student/home.html',{'stats':stats,'comp':comp})

def profile(request):
    student = {
        "name": "Peter Ojo",
        'matric': "222497",
        'department': "Computer Science",
        "level": 500,
        'status': "Active"
    }
    return render(request, 'student/profile.html', {'student':student})

def courses(request):
    course_list = [
        {"code": "CSC401", "title": "Artificial Intelligence", "unit": 3},
        {"code": "CSC402", "title": "Compiler Construction", "unit": 2},
        {"code": "CSC403", "title": "Computer Networks", "unit": 3},
        {"code": "CSC404", "title": "Machine Learning", "unit": 3},
    ]
    return render(request, "student/courses.html", {"courses": course_list})
