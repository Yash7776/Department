from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from .models import Department, User_header_all
import logging

logger = logging.getLogger(__name__)

def login(request, dept_name):
    department = get_object_or_404(Department, dept_name=dept_name)
    
    if request.method == 'POST':
        username = request.POST.get('u_user_id')
        password = request.POST.get('u_password')
        
        if not username or not password:
            return render(request, 'login.html', {
                'department': department,
                'error': 'Username and password are required'
            })

        try:
            # Fetch the user with the given username, line_no=0, and status=1
            base_user = User_header_all.objects.filter(username=username, line_no=0, status=1).first()
            if not base_user:
                logger.debug(f"User not found or inactive: {username}")
                return render(request, 'login.html', {
                    'department': department,
                    'error': 'Invalid username or password'
                })

            # Check if the user's department matches the URL dept_name
            if base_user.department and base_user.department.dept_name != dept_name:
                logger.debug(f"User {username} attempted login from incorrect department URL: {dept_name}")
                return render(request, 'login.html', {
                    'department': department,
                    'error': f"You can only log in from http://127.0.0.1:8000/login/{base_user.department.dept_name}"
                })

            # Verify the password
            if check_password(password, base_user.password):
                # Set basic session variables
                request.session['user_id'] = base_user.user_id
                request.session['user_name'] = base_user.full_name
                request.session['user_designation'] = ''


                # Redirect to dashboard on successful login
                logger.debug(f"Login successful for {username}, redirecting to dashboard")
                return redirect('dashboard', dept_name=dept_name)
            else:
                logger.debug(f"Password mismatch for {username}")
                return render(request, 'login.html', {
                    'department': department,
                    'error': 'Invalid username or password'
                })
        except Exception as e:
            logger.debug(f"Error during login for {username}: {str(e)}")
            return render(request, 'login.html', {
                'department': department,
                'error': 'Invalid username or password'
            })
    
    return render(request, 'login.html', {'department': department})

def dashboard(request, dept_name):
    department = get_object_or_404(Department, dept_name=dept_name)
    # Ensure user is logged in and belongs to the correct department
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login', dept_name=dept_name)
    
    try:
        user = User_header_all.objects.get(user_id=user_id, status=1)
        if user.department.dept_name != dept_name:
            return redirect('login', dept_name=user.department.dept_name)
    except User_header_all.DoesNotExist:
        return redirect('login', dept_name=dept_name)
    
    return render(request, 'dashboard.html', {'department': department})