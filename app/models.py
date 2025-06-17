from django.db import models
from django.urls import reverse
from django.utils import timezone

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
    dept_login_bg = models.ImageField(upload_to='department_backgrounds/login/', null=True, blank=True)  # Background for login page
    dept_dashboard_bg = models.ImageField(upload_to='department_backgrounds/dashboard/', null=True, blank=True)  # Background for dashboard page

    def __str__(self):
        return f"{self.dept_id} - {self.dept_name}"

    def save(self, *args, **kwargs):
        if not self.dept_id:
            unique_id, _ = UniqueIdHeaderAll.objects.get_or_create(
                table_name='department',
                id_for='dept_id',
                defaults={
                    'prefix': 'DEP',
                    'last_id': '',
                    'created_on': timezone.now(),
                    'modified_on': timezone.now()
                }
            )
            self.dept_id = unique_id.get_next_id()

        if not self.link:
            base_url = "http://127.0.0.1:8000"
            path = reverse('login', args=[self.dept_name])
            self.link = f"{base_url}{path}"

        super().save(*args, **kwargs)

    @classmethod
    def get_or_assign_dept_id(cls, dept_name):
        existing_dept = cls.objects.filter(dept_name=dept_name).first()
        if existing_dept:
            return existing_dept.dept_id
        unique_id, _ = UniqueIdHeaderAll.objects.get_or_create(
            table_name='department',
            id_for='dept_id',
            defaults={
                'prefix': 'DEP',
                'last_id': '',
                'created_on': timezone.now(),
                'modified_on': timezone.now()
            }
        )
        return unique_id.get_next_id()