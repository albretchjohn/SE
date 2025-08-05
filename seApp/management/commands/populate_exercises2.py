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
        
        # Get objects for relationships
        strength_type = ExerciseType.objects.get(name='strength')
        cardio_type = ExerciseType.objects.get(name='cardio')
        flexibility_type = ExerciseType.objects.get(name='flexibility')
        
        sedentary_level = ActivityLevel.objects.get(name='sedentary')
        lightly_active_level = ActivityLevel.objects.get(name='lightly_active')
        moderately_active_level = ActivityLevel.objects.get(name='moderately_active')
        very_active_level = ActivityLevel.objects.get(name='very_active')
        extremely_active_level = ActivityLevel.objects.get(name='extremely_active')
        
        # STRENGTH EXERCISES
        strength_exercises_data = [
            # Sedentary - With Equipment
            {'name': 'Leg Press', 'duration': '30 mins', 'reps': 10, 'sets': 3, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Chest Press', 'duration': '30 mins', 'reps': 10, 'sets': 3, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Lat Pulldown', 'duration': '30 mins', 'reps': 10, 'sets': 3, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Seated Row', 'duration': '30 mins', 'reps': 10, 'sets': 3, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Dumbbell Shoulder Press', 'duration': '30 mins', 'reps': 10, 'sets': 3, 'requires_equipment': True, 'activity_level': sedentary_level},
            
            # Sedentary - Without Equipment
            {'name': 'Bodyweight Squats', 'duration': '15 mins', 'reps': 15, 'sets': 3, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'Push-ups', 'duration': '15 mins', 'reps': 15, 'sets': 3, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'Lunges', 'duration': '15 mins', 'reps': 12, 'sets': 3, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'Plank', 'duration': '30 secs', 'reps': 0, 'sets': 3, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'Glute Bridges', 'duration': '15 mins', 'reps': 15, 'sets': 3, 'requires_equipment': False, 'activity_level': sedentary_level},
            
            # Lightly Active - With Equipment
            {'name': 'Dumbbell Rows', 'duration': '5 mins', 'reps': 12, 'sets': 4, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'Tricep Extensions', 'duration': '5 mins', 'reps': 12, 'sets': 4, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'Leg Curl Machine', 'duration': '5 mins', 'reps': 12, 'sets': 4, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'Chest Fly Machine', 'duration': '5 mins', 'reps': 12, 'sets': 4, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'Cable Lateral Raises', 'duration': '5 mins', 'reps': 12, 'sets': 4, 'requires_equipment': True, 'activity_level': lightly_active_level},
            
            # Lightly Active - Without Equipment
            {'name': 'Lunges (LA)', 'duration': '5 mins', 'reps': 20, 'sets': 3, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Planks', 'duration': '3 mins', 'reps': 1, 'sets': 3, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Burpees', 'duration': '3 mins', 'reps': 10, 'sets': 3, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Mountain Climbers', 'duration': '15 mins', 'reps': 30, 'sets': 3, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Supermans', 'duration': '3 mins', 'reps': 15, 'sets': 3, 'requires_equipment': False, 'activity_level': lightly_active_level},
            
            # Moderately Active - With Equipment
            {'name': 'Deadlifts', 'duration': '30 mins', 'reps': 8, 'sets': 4, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Pull-ups', 'duration': '30 mins', 'reps': 8, 'sets': 4, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Barbell Squats', 'duration': '30 mins', 'reps': 10, 'sets': 4, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Bench Press', 'duration': '30 mins', 'reps': 8, 'sets': 4, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Dumbbell Lunges', 'duration': '30 mins', 'reps': 10, 'sets': 3, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Cable Rows', 'duration': '30 mins', 'reps': 10, 'sets': 3, 'requires_equipment': True, 'activity_level': moderately_active_level},
            
            # Moderately Active - Without Equipment
            {'name': 'Jump Squats', 'duration': '20 mins', 'reps': 20, 'sets': 3, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Bicycle Crunches', 'duration': '20 mins', 'reps': 20, 'sets': 3, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Burpees (MA)', 'duration': '20 mins', 'reps': 15, 'sets': 3, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Mountain Climbers (MA)', 'duration': '20 mins', 'reps': 20, 'sets': 3, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Plank to Push-up Transition', 'duration': '2 mins', 'reps': 0, 'sets': 3, 'requires_equipment': False, 'activity_level': moderately_active_level},
            
            # Very Active - With Equipment
            {'name': 'Clean and Press', 'duration': '30 mins', 'reps': 6, 'sets': 5, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Cable Flyes', 'duration': '30 mins', 'reps': 6, 'sets': 5, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Deadlift (VA)', 'duration': '30 mins', 'reps': 6, 'sets': 5, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Barbell Squats (VA)', 'duration': '30 mins', 'reps': 6, 'sets': 5, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Dumbbell Bench Press', 'duration': '30 mins', 'reps': 6, 'sets': 5, 'requires_equipment': True, 'activity_level': very_active_level},
            
            # Very Active - Without Equipment
            {'name': 'Burpees (VA)', 'duration': '25 mins', 'reps': 20, 'sets': 4, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Pike Push-ups', 'duration': '25 mins', 'reps': 20, 'sets': 4, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Handstand Push-ups', 'duration': '25 mins', 'reps': 10, 'sets': 4, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Tuck Jumps', 'duration': '25 mins', 'reps': 15, 'sets': 4, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Box Jumps', 'duration': '25 mins', 'reps': 15, 'sets': 4, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Mountain Climbers (VA)', 'duration': '25 mins', 'reps': 20, 'sets': 4, 'requires_equipment': False, 'activity_level': very_active_level},
            
            # Extremely Active - With Equipment
            {'name': 'Snatch', 'duration': '45 mins', 'reps': 5, 'sets': 5, 'requires_equipment': True, 'activity_level': extremely_active_level},
            {'name': 'Front Squats', 'duration': '45 mins', 'reps': 5, 'sets': 5, 'requires_equipment': True, 'activity_level': extremely_active_level},
            {'name': 'Deadlifts (EA)', 'duration': '45 mins', 'reps': 5, 'sets': 5, 'requires_equipment': True, 'activity_level': extremely_active_level},
            {'name': 'Barbell Bench Press', 'duration': '45 mins', 'reps': 5, 'sets': 5, 'requires_equipment': True, 'activity_level': extremely_active_level},
            {'name': 'Leg Press (EA)', 'duration': '45 mins', 'reps': 10, 'sets': 5, 'requires_equipment': True, 'activity_level': extremely_active_level},
            
            # Extremely Active - Without Equipment
            {'name': 'One-Arm Push-ups', 'duration': '30 mins', 'reps': 10, 'sets': 5, 'requires_equipment': False, 'activity_level': extremely_active_level},
            {'name': 'Handstand Push-ups (EA)', 'duration': '30 mins', 'reps': 10, 'sets': 5, 'requires_equipment': False, 'activity_level': extremely_active_level},
            {'name': 'Burpees (EA)', 'duration': '30 mins', 'reps': 10, 'sets': 5, 'requires_equipment': False, 'activity_level': extremely_active_level},
            {'name': 'Dips', 'duration': '30 mins', 'reps': 8, 'sets': 5, 'requires_equipment': False, 'activity_level': extremely_active_level},
            {'name': 'Plank Jacks', 'duration': '30 mins', 'reps': 0, 'sets': 1, 'requires_equipment': False, 'activity_level': extremely_active_level},
        ]
        
        # CARDIO EXERCISES
        cardio_exercises_data = [
            # Sedentary - With Equipment
            {'name': 'Stationary Bike', 'duration': '20 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Jogging', 'duration': '20 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Elliptical Trainer', 'duration': '20 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Rowing Machine', 'duration': '20 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': sedentary_level},
            
            # Sedentary - Without Equipment
            {'name': 'Walking', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'Jumping Jacks', 'duration': '10 mins', 'reps': 1, 'sets': 5, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'Bodyweight Squats (Cardio)', 'duration': '15 mins', 'reps': 10, 'sets': 3, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'High Knees', 'duration': '10 mins', 'reps': 1, 'sets': 5, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'Burpees (Cardio)', 'duration': '10 mins', 'reps': 1, 'sets': 5, 'requires_equipment': False, 'activity_level': sedentary_level},
            
            # Lightly Active - With Equipment
            {'name': 'Treadmill Jog', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'Stationary Rowing', 'duration': '20 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'Recumbent Bike', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'Stair Climber', 'duration': '20 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'Circuit Training', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': lightly_active_level},
            
            # Lightly Active - Without Equipment
            {'name': 'Light Jogging', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Brisk Walking', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Bodyweight Lunges', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Mountain Climbers (Cardio)', 'duration': '10 mins', 'reps': 0, 'sets': 5, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Zumba', 'duration': '30 mins', 'reps': 0, 'sets': 0, 'requires_equipment': False, 'activity_level': lightly_active_level},
            
            # Moderately Active - With Equipment
            {'name': 'Elliptical', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Stationary Bike (MA)', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Rowing Machine (MA)', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Stair Climber (MA)', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Arc Trainer', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': moderately_active_level},
            
            # Moderately Active - Without Equipment
            {'name': 'Running', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Brisk Walking (MA)', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Jump Rope', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Hiking', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Jumping Jacks (MA)', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': moderately_active_level},
            
            # Very Active - With Equipment
            {'name': 'Rowing Machine (VA)', 'duration': '60 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Treadmill Sprints', 'duration': '60 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'HIIT on Stationary Bike', 'duration': '60 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Battle Ropes', 'duration': '60 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Kettlebell Swings', 'duration': '60 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': very_active_level},
            
            # Very Active - Without Equipment
            {'name': 'Sprint Intervals', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Burpees (VA Cardio)', 'duration': '30 mins', 'reps': 0, 'sets': 0, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Box Jumps (VA)', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Mountain Climbers (VA Cardio)', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Jump Squats (VA)', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': very_active_level},
            
            # Extremely Active - With Equipment
            {'name': 'HIIT on Bike', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': extremely_active_level},
            {'name': 'Rowing Machine Intervals', 'duration': '30 mins', 'reps': 5, 'sets': 1, 'requires_equipment': True, 'activity_level': extremely_active_level},
            {'name': 'Stair Climber Sprints', 'duration': '30 mins', 'reps': 10, 'sets': 1, 'requires_equipment': True, 'activity_level': extremely_active_level},
            {'name': 'Battle Ropes (EA)', 'duration': '30 mins', 'reps': 10, 'sets': 1, 'requires_equipment': True, 'activity_level': extremely_active_level},
            
            # Extremely Active - Without Equipment
            {'name': 'HIIT Running', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': extremely_active_level},
            {'name': 'Burpees (EA Cardio)', 'duration': '20 mins', 'reps': 20, 'sets': 3, 'requires_equipment': False, 'activity_level': extremely_active_level},
            {'name': 'Mountain Climbers (EA)', 'duration': '15 mins', 'reps': 0, 'sets': 3, 'requires_equipment': False, 'activity_level': extremely_active_level},
        ]
        
        # FLEXIBILITY EXERCISES
        flexibility_exercises_data = [
            # Sedentary - With Equipment
            {'name': 'Resistance Band Stretching', 'duration': '15 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Foam Roller Stretching', 'duration': '10 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Yoga Wheel Stretch', 'duration': '15 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Resistance Band Hamstring Stretch', 'duration': '15 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Stability Ball Back Stretch', 'duration': '15 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': sedentary_level},
            {'name': 'Dumbbell Overhead Tricep Stretch', 'duration': '5 mins', 'reps': 2, 'sets': 1, 'requires_equipment': True, 'activity_level': sedentary_level},
            
            # Sedentary - Without Equipment
            {'name': 'Basic Yoga', 'duration': '20 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'Seated Forward Bend', 'duration': '5 mins', 'reps': 2, 'sets': 1, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'Cat-Cow Stretch', 'duration': '5 mins', 'reps': 10, 'sets': 1, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'Standing Quadriceps Stretch', 'duration': '5 mins', 'reps': 2, 'sets': 1, 'requires_equipment': False, 'activity_level': sedentary_level},
            {'name': 'Lying Spinal Twist', 'duration': '5 mins', 'reps': 2, 'sets': 1, 'requires_equipment': False, 'activity_level': sedentary_level},
            
            # Lightly Active - With Equipment
            {'name': 'Foam Rolling', 'duration': '20 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'Resistance Band Shoulder Stretch', 'duration': '10 mins', 'reps': 2, 'sets': 1, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'Weighted Hip Flexor Stretch', 'duration': '15 mins', 'reps': 2, 'sets': 1, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'Cable Machine Chest Stretch', 'duration': '10 mins', 'reps': 2, 'sets': 1, 'requires_equipment': True, 'activity_level': lightly_active_level},
            {'name': 'TRX Hamstring Stretch', 'duration': '10 mins', 'reps': 2, 'sets': 1, 'requires_equipment': True, 'activity_level': lightly_active_level},
            
            # Lightly Active - Without Equipment
            {'name': 'Intermediate Yoga', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Pigeon Pose', 'duration': '5 mins', 'reps': 0, 'sets': 0, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Lizard Pose', 'duration': '5 mins', 'reps': 0, 'sets': 0, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Cobra Stretch', 'duration': '5 mins', 'reps': 0, 'sets': 0, 'requires_equipment': False, 'activity_level': lightly_active_level},
            {'name': 'Seated Straddle Stretch', 'duration': '5 mins', 'reps': 0, 'sets': 0, 'requires_equipment': False, 'activity_level': lightly_active_level},
            
            # Moderately Active - With Equipment
            {'name': 'Dynamic Stretching', 'duration': '25 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Foam Roller Stretching (MA)', 'duration': '20 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Resistance Band Hamstring Stretch (MA)', 'duration': '15 mins', 'reps': 3, 'sets': 1, 'requires_equipment': True, 'activity_level': moderately_active_level},
            {'name': 'Stability Ball Back Stretch (MA)', 'duration': '10 mins', 'reps': 5, 'sets': 1, 'requires_equipment': True, 'activity_level': moderately_active_level},
            
            # Moderately Active - Without Equipment
            {'name': 'Advanced Yoga', 'duration': '40 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Standing Quadriceps Stretch (MA)', 'duration': '10 mins', 'reps': 3, 'sets': 1, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Seated Forward Bend (MA)', 'duration': '15 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Cat-Cow Stretch (MA)', 'duration': '10 mins', 'reps': 10, 'sets': 1, 'requires_equipment': False, 'activity_level': moderately_active_level},
            {'name': 'Lying Spinal Twist (MA)', 'duration': '10 mins', 'reps': 3, 'sets': 1, 'requires_equipment': False, 'activity_level': moderately_active_level},
            
            # Very Active - With Equipment
            {'name': 'Pilates with Equipment', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Foam Roller IT Band Stretch', 'duration': '15 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Cable Chest Stretch', 'duration': '10 mins', 'reps': 3, 'sets': 1, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Resistance Band Shoulder Stretch (VA)', 'duration': '10 mins', 'reps': 3, 'sets': 1, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Yoga Wheel Backbend', 'duration': '15 mins', 'reps': 5, 'sets': 1, 'requires_equipment': True, 'activity_level': very_active_level},
            {'name': 'Weighted Hip Flexor Stretch (VA)', 'duration': '10 mins', 'reps': 3, 'sets': 1, 'requires_equipment': True, 'activity_level': very_active_level},
            
            # Very Active - Without Equipment
            {'name': 'Pilates', 'duration': '45 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Dynamic Lunge with Twist', 'duration': '10 mins', 'reps': 10, 'sets': 2, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Pigeon Pose (VA)', 'duration': '10 mins', 'reps': 1, 'sets': 2, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Bridge Pose', 'duration': '10 mins', 'reps': 1, 'sets': 2, 'requires_equipment': False, 'activity_level': very_active_level},
            {'name': 'Standing Forward Bend', 'duration': '10 mins', 'reps': 1, 'sets': 2, 'requires_equipment': False, 'activity_level': very_active_level},
            
            # Extremely Active - With Equipment
            {'name': 'Extreme Stretching', 'duration': '60 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': extremely_active_level},
            {'name': 'Foam Roller Stretching (EA)', 'duration': '30 mins', 'reps': 1, 'sets': 1, 'requires_equipment': True, 'activity_level': extremely_active_level},
            {'name': 'Resistance Band Hamstring Stretch (EA)', 'duration': '15 mins', 'reps': 3, 'sets': 2, 'requires_equipment': True, 'activity_level': extremely_active_level},
            {'name': 'Weighted Forward Bend', 'duration': '20 mins', 'reps': 10, 'sets': 2, 'requires_equipment': True, 'activity_level': extremely_active_level},
            
            # Extremely Active - Without Equipment
            {'name': 'Power Yoga', 'duration': '60 mins', 'reps': 1, 'sets': 1, 'requires_equipment': False, 'activity_level': extremely_active_level},
            {'name': 'Dynamic Leg Swings', 'duration': '10 mins', 'reps': 10, 'sets': 2, 'requires_equipment': False, 'activity_level': extremely_active_level},
            {'name': 'Seated Straddle Stretch (EA)', 'duration': '15 mins', 'reps': 1, 'sets': 2, 'requires_equipment': False, 'activity_level': extremely_active_level},
            {'name': 'Cat-Cow Stretch (EA)', 'duration': '10 mins', 'reps': 10, 'sets': 2, 'requires_equipment': False, 'activity_level': extremely_active_level},
        ]

        # Insert all exercises
        all_exercises = [
            (strength_exercises_data, strength_type),
            (cardio_exercises_data, cardio_type),
            (flexibility_exercises_data, flexibility_type),
        ]

        for exercise_list, exercise_type in all_exercises:
            for exercise_data in exercise_list:
                Exercise.objects.get_or_create(
                    name=exercise_data['name'],
                    exercise_type=exercise_type,
                    activity_level=exercise_data['activity_level'],
                    requires_equipment=exercise_data['requires_equipment'],
                    defaults={
                        'duration': exercise_data['duration'],
                        'reps': exercise_data['reps'],
                        'sets': exercise_data['sets']
                    }
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated exercise database!')
        )