from django.shortcuts import render, get_object_or_404, redirect
from .models import Department

def login(request, dept_name):
    department = get_object_or_404(Department, dept_name=dept_name)
    if request.method == 'POST':
        # Basic login validation (replace with actual authentication logic)
        username = request.POST.get('u_user_id')
        password = request.POST.get('u_password')
        # Example: Replace with real authentication (e.g., Django auth)
        if username and password:  # Simulate successful login
            return redirect('dashboard', dept_name=dept_name)
        else:
            return render(request, 'login.html', {
                'department': department,
                'error': 'Invalid username or password'
            })
    return render(request, 'login.html', {'department': department})

def dashboard(request, dept_name):
    department = get_object_or_404(Department, dept_name=dept_name)
    return render(request, 'dashboard.html', {'department': department})