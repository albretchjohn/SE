from django.core.management.base import BaseCommand
from seApp.models import ActivityLevel, ExerciseType, Exercise

class Command(BaseCommand):
    help = 'Populate exercise database with strength training exercises by activity level and equipment requirement'

    def handle(self, *args, **options):
        # Define activity levels and create them
        activity_levels = [
            ('sedentary', 'Sedentary'),
            ('lightly_active', 'Lightly Active'),
            ('moderately_active', 'Moderately Active'),
            ('very_active', 'Very Active'),
            ('extremely_active', 'Extremely Active'),
        ]

        for code, name in activity_levels:
            ActivityLevel.objects.get_or_create(name=code, defaults={'display_name': name})

        # Define exercise types and create them
        ExerciseType.objects.get_or_create(name='strength', defaults={'display_name': 'Strength Training'})

        # Get the strength type
        strength_type = ExerciseType.objects.get(name='strength')

        # Strength exercises organized by activity level and equipment use
        strength_exercises = {
            'sedentary': {
                True: [
                    {'name': 'Leg Press', 'duration': '30 mins', 'reps': 10, 'sets': 3},
                    {'name': 'Chest Press', 'duration': '30 mins', 'reps': 10, 'sets': 3},
                    {'name': 'Lat Pulldown', 'duration': '30 mins', 'reps': 10, 'sets': 3},
                    {'name': 'Seated Row', 'duration': '30 mins', 'reps': 10, 'sets': 3},
                    {'name': 'Dumbbell Shoulder Press', 'duration': '30 mins', 'reps': 10, 'sets': 3},
                ],
                False: [
                    {'name': 'Bodyweight Squats', 'duration': '15 mins', 'reps': 15, 'sets': 3},
                    {'name': 'Push-ups', 'duration': '15 mins', 'reps': 15, 'sets': 3},
                    {'name': 'Lunges', 'duration': '15 mins', 'reps': 12, 'sets': 3},
                    {'name': 'Plank', 'duration': '30 secs', 'reps': 0, 'sets': 3},
                    {'name': 'Glute Bridges', 'duration': '15 mins', 'reps': 15, 'sets': 3},
                ]
            },
            'lightly_active': {
                True: [
                    {'name': 'Dumbbell Rows', 'duration': '5 mins', 'reps': 12, 'sets': 4},
                    {'name': 'Tricep Extensions', 'duration': '5 mins', 'reps': 12, 'sets': 4},
                    {'name': 'Leg Curl Machine', 'duration': '5 mins', 'reps': 12, 'sets': 4},
                    {'name': 'Chest Fly Machine', 'duration': '5 mins', 'reps': 12, 'sets': 4},
                    {'name': 'Cable Lateral Raises', 'duration': '5 mins', 'reps': 12, 'sets': 4},
                ],
                False: [
                    {'name': 'Lunges', 'duration': '5 mins', 'reps': 20, 'sets': 3},
                    {'name': 'Planks', 'duration': '3 mins', 'reps': 1, 'sets': 3},
                    {'name': 'Burpees', 'duration': '3 mins', 'reps': 10, 'sets': 3},
                    {'name': 'Mountain Climbers', 'duration': '15 mins', 'reps': 30, 'sets': 3},
                    {'name': 'Supermans', 'duration': '3 mins', 'reps': 15, 'sets': 3},
                ]
            },
            'moderately_active': {
                True: [
                    {'name': 'Deadlifts', 'duration': '30 mins', 'reps': 8, 'sets': 4},
                    {'name': 'Pull-ups', 'duration': '30 mins', 'reps': 8, 'sets': 4},
                    {'name': 'Barbell Squats', 'duration': '30 mins', 'reps': 10, 'sets': 4},
                    {'name': 'Bench Press', 'duration': '30 mins', 'reps': 8, 'sets': 4},
                    {'name': 'Dumbbell Lunges', 'duration': '30 mins', 'reps': 10, 'sets': 3},
                    {'name': 'Cable Rows', 'duration': '30 mins', 'reps': 10, 'sets': 3},
                ],
                False: [
                    {'name': 'Jump Squats', 'duration': '20 mins', 'reps': 20, 'sets': 3},
                    {'name': 'Bicycle Crunches', 'duration': '20 mins', 'reps': 20, 'sets': 3},
                    {'name': 'Burpees', 'duration': '20 mins', 'reps': 15, 'sets': 3},
                    {'name': 'Mountain Climbers', 'duration': '20 mins', 'reps': 20, 'sets': 3},
                    {'name': 'Plank to Push-up Transition', 'duration': '2 mins', 'reps': 0, 'sets': 3},
                ]
            },
            'very_active': {
                True: [
                    {'name': 'Clean and Press', 'duration': '30 mins', 'reps': 6, 'sets': 5},
                    {'name': 'Cable Flyes', 'duration': '30 mins', 'reps': 6, 'sets': 5},
                    {'name': 'Deadlift', 'duration': '30 mins', 'reps': 6, 'sets': 5},
                    {'name': 'Barbell Squats', 'duration': '30 mins', 'reps': 6, 'sets': 5},
                    {'name': 'Dumbbell Bench Press', 'duration': '30 mins', 'reps': 6, 'sets': 5},
                ],
                False: [
                    {'name': 'Burpees', 'duration': '25 mins', 'reps': 20, 'sets': 4},
                    {'name': 'Pike Push-ups', 'duration': '25 mins', 'reps': 20, 'sets': 4},
                    {'name': 'Handstand Push-ups', 'duration': '25 mins', 'reps': 10, 'sets': 4},
                    {'name': 'Tuck Jumps', 'duration': '25 mins', 'reps': 15, 'sets': 4},
                    {'name': 'Box Jumps', 'duration': '25 mins', 'reps': 15, 'sets': 4},
                    {'name': 'Mountain Climbers', 'duration': '25 mins', 'reps': 20, 'sets': 4},
                ]
            },
            'extremely_active': {
                True: [
                    {'name': 'Snatch', 'duration': '45 mins', 'reps': 5, 'sets': 5},
                    {'name': 'Front Squats', 'duration': '45 mins', 'reps': 5, 'sets': 5},
                    {'name': 'Deadlifts', 'duration': '45 mins', 'reps': 5, 'sets': 5},
                    {'name': 'Barbell Bench Press', 'duration': '45 mins', 'reps': 5, 'sets': 5},
                    {'name': 'Leg Press', 'duration': '45 mins', 'reps': 10, 'sets': 5},
                ],
                False: [
                    {'name': 'One-Arm Push-ups', 'duration': '30 mins', 'reps': 10, 'sets': 5},
                    {'name': 'Handstand Push-ups', 'duration': '30 mins', 'reps': 10, 'sets': 5},
                    {'name': 'Burpees', 'duration': '30 mins', 'reps': 10, 'sets': 5},
                    {'name': 'Dips', 'duration': '30 mins', 'reps': 8, 'sets': 5},
                    {'name': 'Plank Jacks', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                ]
            }
        }

        # Insert all exercises into the database
        for level_code, equipment_map in strength_exercises.items():
            activity_level = ActivityLevel.objects.get(name=level_code)
            for requires_equipment, exercises in equipment_map.items():
                for exercise in exercises:
                    Exercise.objects.get_or_create(
                        name=exercise['name'],
                        exercise_type=strength_type,
                        activity_level=activity_level,
                        requires_equipment=requires_equipment,
                        defaults={
                            'duration': exercise['duration'],
                            'reps': exercise['reps'],
                            'sets': exercise['sets']
                        }
                    )
