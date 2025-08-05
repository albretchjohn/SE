from django.core.management.base import BaseCommand
from seApp.models import ActivityLevel, ExerciseType, Exercise

class Command(BaseCommand):
    help = 'Populate exercise database with strength, cardio, and flexibility exercises by activity level and equipment requirement'

    def handle(self, *args, **options):
        # Define and create activity levels
        activity_levels = [
            ('sedentary', 'Sedentary'),
            ('lightly_active', 'Lightly Active'),
            ('moderately_active', 'Moderately Active'),
            ('very_active', 'Very Active'),
            ('extremely_active', 'Extremely Active'),
        ]

        for code, name in activity_levels:
            ActivityLevel.objects.get_or_create(name=code, defaults={'display_name': name})

        # Define and create exercise types
        for code, name in [
            ('strength', 'Strength Training'),
            ('cardio', 'Cardiovascular'),
            ('flexibility', 'Flexibility & Mobility'),
        ]:
            ExerciseType.objects.get_or_create(name=code, defaults={'display_name': name})

        # Fetch the exercise types
        strength_type = ExerciseType.objects.get(name='strength')
        cardio_type = ExerciseType.objects.get(name='cardio')
        flexibility_type = ExerciseType.objects.get(name='flexibility')

        # ==== Strength Exercises ====
        strength_exercises = { ... }  # use your latest version (already structured)

        # ==== Cardio Exercises ====
        cardio_exercises = {
            'sedentary': {
                True: [
                    {'name': 'Stationary Bike', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Treadmill Walk', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                ],
                False: [
                    {'name': 'Walking', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Marching in Place', 'duration': '20 mins', 'reps': 0, 'sets': 1},
                ]
            },
            'lightly_active': {
                True: [
                    {'name': 'Elliptical Trainer', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Treadmill Jogging', 'duration': '25 mins', 'reps': 0, 'sets': 1},
                ],
                False: [
                    {'name': 'Jogging', 'duration': '25 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Jumping Jacks', 'duration': '20 mins', 'reps': 30, 'sets': 3},
                ]
            },
            'moderately_active': {
                True: [
                    {'name': 'Spinning Class', 'duration': '45 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Rowing Machine', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                ],
                False: [
                    {'name': 'Running', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                    {'name': 'High Knees', 'duration': '20 mins', 'reps': 30, 'sets': 3},
                ]
            },
            'very_active': {
                True: [
                    {'name': 'Treadmill Sprints', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Stair Climber', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                ],
                False: [
                    {'name': 'Jump Rope', 'duration': '20 mins', 'reps': 50, 'sets': 3},
                    {'name': 'Burpees', 'duration': '25 mins', 'reps': 20, 'sets': 3},
                ]
            },
            'extremely_active': {
                True: [
                    {'name': 'HIIT on Treadmill', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Sled Push', 'duration': '20 mins', 'reps': 0, 'sets': 1},
                ],
                False: [
                    {'name': 'HIIT Circuit', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Sprint Intervals', 'duration': '20 mins', 'reps': 0, 'sets': 1},
                ]
            }
        }

        # ==== Flexibility Exercises ====
        flexibility_exercises = {
            'sedentary': {
                True: [],
                False: [
                    {'name': 'Seated Forward Bend', 'duration': '10 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Neck Rolls', 'duration': '5 mins', 'reps': 0, 'sets': 1},
                ]
            },
            'lightly_active': {
                True: [],
                False: [
                    {'name': 'Standing Hamstring Stretch', 'duration': '5 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Child’s Pose', 'duration': '5 mins', 'reps': 0, 'sets': 1},
                ]
            },
            'moderately_active': {
                True: [],
                False: [
                    {'name': 'Downward Dog', 'duration': '10 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Quad Stretch', 'duration': '5 mins', 'reps': 0, 'sets': 1},
                ]
            },
            'very_active': {
                True: [],
                False: [
                    {'name': 'Lunge with Spinal Twist', 'duration': '10 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Butterfly Stretch', 'duration': '10 mins', 'reps': 0, 'sets': 1},
                ]
            },
            'extremely_active': {
                True: [],
                False: [
                    {'name': 'Pigeon Pose', 'duration': '10 mins', 'reps': 0, 'sets': 1},
                    {'name': 'Advanced Yoga Flow', 'duration': '30 mins', 'reps': 0, 'sets': 1},
                ]
            }
        }

        # ====== Helper to insert exercises ======
        def insert_exercises(exercise_dict, exercise_type):
            for level_code, equipment_map in exercise_dict.items():
                activity_level = ActivityLevel.objects.get(name=level_code)
                for requires_equipment, exercises in equipment_map.items():
                    for exercise in exercises:
                        Exercise.objects.get_or_create(
                            name=exercise['name'],
                            exercise_type=exercise_type,
                            activity_level=activity_level,
                            requires_equipment=requires_equipment,
                            defaults={
                                'duration': exercise['duration'],
                                'reps': exercise['reps'],
                                'sets': exercise['sets']
                            }
                        )

        # Insert all exercise categories
        insert_exercises(strength_exercises, strength_type)
        insert_exercises(cardio_exercises, cardio_type)
        insert_exercises(flexibility_exercises, flexibility_type)
