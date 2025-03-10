from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('user', 'User'),
        ('faculty', 'Faculty'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )
    
    def __str__(self):
        return self.username
    '''
    def set_password(self, raw_password):
        """Override Django's default password hashing to store plain text passwords."""
        self.password = raw_password  # Stores password as plain text
        self._password = raw_password
        self.save()
    '''


class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

class Profile(models.Model):
   
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    college_department = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField(default=0)
    body_type = models.CharField(max_length=20)
    activity_level = models.CharField(max_length=20)
    equipment_access = models.TextField()
    health_condition = models.TextField()
    allergies = models.TextField()
    injuries = models.TextField()
    
    def __str__(self):
        return f"Profile of {self.user.username}"

class DietPlan(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    calorie_intake_per_day = models.IntegerField()
    fats_per_meal = models.FloatField()
    carbs_per_meal = models.FloatField()
    protein_per_meal = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self): 
        return f"{self.user.username}'s Exercise Plan"
    
    class Meta: 
        
        indexes = [ models.Index(fields=['user', 'status']), ]

class ExercisePlan(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    strength_exercises = models.TextField()
    flexibility_exercises = models.TextField()
    cardio_exercises = models.TextField()
    routine = models.JSONField()
    rest_day = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.user.username}'s Exercise Plan"
    
    class Meta: 
        
        indexes = [ models.Index(fields=['user', 'status']), ]


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

class E_PlanApproval(models.Model):
    E_plan = models.ForeignKey(ExercisePlan, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    review_comments = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f"Approval by {self.faculty.name} for {self.E_plan}"

class D_PlanApproval(models.Model):
    D_plan = models.ForeignKey(DietPlan, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    review_comments = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)

