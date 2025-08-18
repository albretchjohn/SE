from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings

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
    bmi_classification = models.TextField()
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
    reviewed_by_fullname_he = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self): 
        return f"{self.user.username}'s Exercise Plan"
    
    class Meta: 
        
        indexes = [ models.Index(fields=['user', 'status']), ]

class ExercisePlan(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_day = models.TextField(null=True, blank=True)
    second_day = models.TextField(null=True, blank=True)
    third_day = models.TextField(null=True, blank=True)
    fourth_day = models.TextField(null=True, blank=True)
    fifth_day = models.TextField(null=True, blank=True)
    sixth_day = models.TextField(null=True, blank=True)
    strength_exercises = models.TextField()
    flexibility_exercises = models.TextField()
    cardio_exercises = models.TextField()
    routine = models.JSONField()
    rest_day = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')
    reviewed_by_fullname_csspe = models.CharField(max_length=255, null=True, blank=True)
    reviewed_by_fullname_he = models.CharField(max_length=255, null=True, blank=True)

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

class WeightEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.weight} kg on {self.date_logged.date()}"
    
    
    
    


############################################

class ActivityLevel(models.Model):
    ACTIVITY_CHOICES = [
        ('sedentary', 'Sedentary'),
        ('lightly_active', 'Lightly Active'),
        ('moderately_active', 'Moderately Active'),
        ('very_active', 'Very Active'),
        ('extremely_active', 'Extremely Active'),
    ]
    name = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, unique=True)
    display_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.display_name

class ExerciseType(models.Model):
    TYPE_CHOICES = [
        ('strength', 'Strength'),
        ('cardio', 'Cardio'),
        ('flexibility', 'Flexibility'),
    ]
    name = models.CharField(max_length=20, choices=TYPE_CHOICES, unique=True)
    display_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.display_name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    activity_level = models.ForeignKey(ActivityLevel, on_delete=models.CASCADE)
    requires_equipment = models.BooleanField(default=False)
    duration = models.CharField(max_length=20)  # e.g., "30 mins", "2 mins"
    reps = models.IntegerField(default=0)
    sets = models.IntegerField(default=1)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['name', 'exercise_type', 'activity_level', 'requires_equipment']
    
    def __str__(self):
        return f"{self.name} ({self.activity_level.display_name})"

