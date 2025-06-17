class Department(models.Model):
    dept_id = models.CharField(max_length=20, unique=True, blank=True)  # Changed from CharField with manual input
    dept_name = models.CharField(max_length=100, unique=True)
    dept_full_name = models.CharField(max_length=100, unique=True)
    dept_logo = models.ImageField(upload_to='department_logos/', null=True, blank=True)
    dept_no_of_projects = models.PositiveIntegerField(default=0)
    dept_reg_contractors = models.PositiveIntegerField(default=0)
    dept_status = models.IntegerField(choices=[(0, 'Suspend'), (1, 'Active')], default=1)
    dept_admins_users = models.PositiveIntegerField(default=0)
    dept_action = models.IntegerField(choices=[(0, 'Suspend'), (1, 'Active')], default=1)  # remove it later
    login_image = models.ImageField(upload_to='department_login_images/', null=True, blank=True)
    dashboard_image = models.ImageField(upload_to='department_dashboard_images/', null=True, blank=True)
    web_link = models.URLField(null=True, blank=True)

class Department(models.Model):
    dept_id = models.CharField(max_length=20, unique=True, blank=True)
    dept_name = models.CharField(max_length=100, unique=True)
    dept_full_name = models.CharField(max_length=100, unique=True)
    dept_logo = models.ImageField(upload_to='department_logos/', null=True, blank=True)
    dept_no_of_projects = models.PositiveIntegerField(default=0)
    dept_reg_contractors = models.PositiveIntegerField(default=0)
    dept_status = models.IntegerField(choices=[(0, 'Suspend'), (1, 'Active')], default=1)
    dept_admins_users = models.PositiveIntegerField(default=0)
    link = models.URLField(max_length=200, blank=True)
    dept_login_bg = models.ImageField(upload_to='department_backgrounds/login/', null=True, blank=True)  #
    dept_dashboard_bg = models.ImageField(upload_to='department_backgrounds/dashboard/', null=True, blank=True)  #