from django.db import models
from django.contrib.auth.models import User
from django import forms


class College(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

# Course model
class Course(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Alumni model (extended user model)
class Alumni(models.Model):
    
    name = models.CharField(max_length=100, default="Default Name") 
    email = models.EmailField(default="default@example.com")
    phonenumber = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile_images/', default='default.jpg')
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year_of_passout = models.IntegerField()

    def __str__(self):
        return self.name


    
    
class Job(models.Model):
    job_title = models.CharField(max_length=255)  # Required field
    description = models.TextField()  # Required field
    company = models.CharField(max_length=255)  # Required field
    place = models.CharField(max_length=255, blank=True)  # Optional field
    last_date = models.DateField()  # Required field
    company_website = models.URLField()  # Required field
    company_image = models.ImageField(upload_to='company_images/', blank=True, null=True)  # Optional field

    def __str__(self):
        return self.job_title
    

    
class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, )  # Set a default value here
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"
    
    
class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    
    
    
    
    
    
    
    
