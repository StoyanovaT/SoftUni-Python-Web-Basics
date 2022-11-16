from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from models_demos.web.models import Employee, Department, Project


def index(request):
    employees = Employee.objects.all()
    # employees2 = Employee.objects.filter(department_id=2)\
    #     .order_by('last_name', 'first_name')

    employees2 = Employee.objects.filter(department__name='Engineering') \
        .order_by('last_name', 'first_name')

    # get_object_or_404(Employee, level=Employee.LEVEL_REGULAR)
    Employee.objects.filter(level=Employee.LEVEL_SENIOR).first()

    department = Department.objects.get(pk=5)
    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    return render(request, 'index.html', context)


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug)
    }
    return render(request, 'department-details.html', context)

def delete_employee(request, pk):
    department_pk = 5

    # When 'Restricted' this must be done explicitly
    # When 'Cascade' this is done implicitly
    Employee.objects.filter(department_id=department_pk).delete()
    get_object_or_404(Department, pk=department_pk).delete()

    # employee = get_object_or_404(Employee, pk=pk)
    # employee.delete()
    # # Deletes all projects with this criteria
    # Project.objects.filter().delete()
    #
    # # Deletes all projects
    # Project.objects.all().delete()
    #
    return redirect('index')
