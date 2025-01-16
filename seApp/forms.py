
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name', 'last_name', 'middle_initial', 'college_department', 'birthday', 
            'gender', 'height', 'weight', 'body_type', 'activity_level', 'equipment_access',
            'health_condition', 'allergies', 'injuries'
        ]
