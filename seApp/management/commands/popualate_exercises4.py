from django.core.management.base import BaseCommand
from seApp.models import ActivityLevel, ExerciseType, Exercise

class Command(BaseCommand):
    help = 'Populate exercise database with strength, cardio, and flexibility exercises by activity level and equipment requirement'

    def handle(self, *args, **options):
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
        types = [
            ('strength', 'Strength Training'),
            ('cardio', 'Cardio'),
            ('flexibility', 'Flexibility')
        ]

        for type_name, display_name in types:
            ExerciseType.objects.get_or_create(name=type_name, defaults={'display_name': display_name})

        # Get exercise type instances
        strength_type = ExerciseType.objects.get(name='strength')
        cardio_type = ExerciseType.objects.get(name='cardio')
        flexibility_type = ExerciseType.objects.get(name='flexibility')

        # Define data (imported or copy-pasted from your structured dictionaries)
        strength_exercises = { ... }  # same structure as provided above
        cardio_exercises = { ... }    # you have this in context
        flexibility_exercises = { ... }  # also in context

        def insert_exercises(exercises_dict, exercise_type):
            for level_code, equipment_map in exercises_dict.items():
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

        insert_exercises(strength_exercises, strength_type)
        insert_exercises(cardio_exercises, cardio_type)
        insert_exercises(flexibility_exercises, flexibility_type)
