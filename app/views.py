from django.shortcuts import render, get_object_or_404
from .models import Department

def login(request, org):
    department = get_object_or_404(Department, org_id=org)
    return render(request, 'login.html', {'department': department})