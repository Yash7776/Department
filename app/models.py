from django.db import models
from django.urls import reverse

class Department(models.Model):
    org_id = models.CharField(max_length=50, unique=True)  # e.g., 'msrdc', 'sidco'
    name = models.CharField(max_length=100)  # e.g., 'Maharashtra State Road Development Corporation Limited'
    logo = models.ImageField(upload_to='department_logos/', null=True, blank=True)  # Store uploaded logo images
    link = models.URLField(max_length=200, blank=True)  # Auto-generated URL field

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate the link using the org_id
        if not self.link:  # Only set the link if it's not already set
            base_url = "http://127.0.0.1:8000"  # Base domain (adjust for production)
            path = reverse('login', args=[self.org_id])  # Resolve the URL pattern for 'login'
            self.link = f"{base_url}{path}"  # Combine to form the full URL
        super().save(*args, **kwargs)