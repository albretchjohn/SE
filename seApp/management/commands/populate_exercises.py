from django.core.management.base import BaseCommand
from seApp.models import ActivityLevel, ExerciseType, Exercise

class Command(BaseCommand):
    help = 'Populate exercise database with initial data'
    
    def handle(self, *args, **options):
        # Create activity levels
        activity_levels = [
            ('sedentary', 'Sedentary'),
            ('lightly_active', 'Lightly Active'),
            ('moderately_active', 'Moderately Active'),
            ('very_active', 'Very Active'),
            ('extremely_active', 'Extremely Active'),
        ]
        
        for code, name in activity_levels:
            ActivityLevel.objects.get_or_create(name=code, defaults={'display_name': name})
        
        # Create exercise types
        exercise_types = [
            ('strength', 'Strength Training'),
            ('cardio', 'Cardiovascular'),
            ('flexibility', 'Flexibility & Mobility'),
        ]
        
        for code, name in exercise_types:
            ExerciseType.objects.get_or_create(name=code, defaults={'display_name': name})
        
        # Your existing data would be inserted here
        # Example for strength exercises:
        strength_type = ExerciseType.objects.get(name='strength')
        sedentary_level = ActivityLevel.objects.get(name='sedentary')
        
        strength_exercises_data = [
            {'name': 'Leg Press', 'duration': '30 mins', 'reps': 10, 'sets': 3, 'requires_equipment': True},
            {'name': 'Bodyweight Squats', 'duration': '15 mins', 'reps': 15, 'sets': 3, 'requires_equipment': False},
            # ... add all your exercises
            
            
        ]
        
        for exercise_data in strength_exercises_data:
            Exercise.objects.get_or_create(
                name=exercise_data['name'],
                exercise_type=strength_type,
                activity_level=sedentary_level,
                requires_equipment=exercise_data['requires_equipment'],
                defaults={
                    'duration': exercise_data['duration'],
                    'reps': exercise_data['reps'],
                    'sets': exercise_data['sets']
                }
            )