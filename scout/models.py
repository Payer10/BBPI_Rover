from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    session = models.CharField(max_length=20, null=True, blank=True)
    depertment = models.CharField(max_length=100, null=True, blank=True)
    bsid = models.CharField(max_length=20, null=True, blank=True)
    student_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name



class Event(models.Model):
    image = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, null=True, blank=True)
    year = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
