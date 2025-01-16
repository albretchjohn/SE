strength_exercises = {
    'sedentary': {
        'with_equipment': [
            {'name': 'Leg Press', 'duration': '30 mins', 'reps': 10, 'sets': 3},
            {'name': 'Chest Press', 'duration': '30 mins', 'reps': 10, 'sets': 3},
            {'name': 'Lat Pulldown', 'duration': '30 mins', 'reps': 10, 'sets': 3},
            {'name': 'Seated Row', 'duration': '30 mins', 'reps': 10, 'sets': 3},
            {'name': 'Dumbbell Shoulder Press', 'duration': '30 mins', 'reps': 10, 'sets': 3},
        ],
        'without_equipment': [
            {'name': 'Bodyweight Squats', 'duration': '15 mins', 'reps': 15, 'sets': 3},
            {'name': 'Push-ups', 'duration': '15 mins', 'reps': 15, 'sets': 3},
            {'name': 'Lunges', 'duration': '15 mins', 'reps': 12, 'sets': 3},
            {'name': 'Plank', 'duration': '30 secs', 'reps': 0, 'sets': 3},
            {'name': 'Glute Bridges', 'duration': '15 mins', 'reps': 15, 'sets': 3},

        ]
    },
    'lightly_active': {
        'with_equipment': [
            {'name': 'Dumbbell Rows', 'duration': '5 mins', 'reps': 12, 'sets': 4},
            {'name': 'Tricep Extensions', 'duration': '5 mins', 'reps': 12, 'sets': 4},
            {'name': 'Leg Curl Machine', 'duration': '5 mins', 'reps': 12, 'sets': 4},
            {'name': 'Chest Fly Machine', 'duration': '5 mins', 'reps': 12, 'sets': 4},
            {'name': 'Cable Lateral Raises', 'duration': '5 mins', 'reps': 12, 'sets': 4},
        ],
        'without_equipment': [
            {'name': 'Lunges', 'duration': '5 mins', 'reps': 20, 'sets': 3},
            {'name': 'Planks', 'duration': '3 mins', 'reps': 1, 'sets': 3},
            {'name': 'Burpees', 'duration': '3 mins', 'reps': 10, 'sets': 3},
            {'name': 'Mountain Climbers', 'duration': '15 mins', 'reps': 30, 'sets': 3},
            {'name': 'Supermans', 'duration': '3 mins', 'reps': 15, 'sets': 3},
        ]
    },
    'moderately_active': {
        'with_equipment': [
            {'name': 'Deadlifts', 'duration': '30 mins', 'reps': 8, 'sets': 4},
            {'name': 'Pull-ups', 'duration': '30 mins', 'reps': 8, 'sets': 4},
            {'name': 'Barbell Squats', 'duration': '30 mins', 'reps': 10, 'sets': 4},
            {'name': 'Bench Press', 'duration': '30 mins', 'reps': 8, 'sets': 4},
            {'name': 'Dumbbell Lunges', 'duration': '30 mins', 'reps': 10, 'sets': 3},
            {'name': 'Cable Rows', 'duration': '30 mins', 'reps': 10, 'sets': 3},

        ],
        'without_equipment': [
            {'name': 'Jump Squats', 'duration': '20 mins', 'reps': 20, 'sets': 3},
            {'name': 'Bicycle Crunches', 'duration': '20 mins', 'reps': 20, 'sets': 3},
            {'name': 'Burpees', 'duration': '20 mins', 'reps': 15, 'sets': 3},
            {'name': 'Mountain Climbers', 'duration': '20 mins', 'reps': 20, 'sets': 3},
            {'name': 'Plank to Push-up Transition', 'duration': '2 mins', 'reps': 0, 'sets': 3},
        ]
    },
    'very_active': {
        'with_equipment': [
            {'name': 'Clean and Press', 'duration': '30 mins', 'reps': 6, 'sets': 5},
            {'name': 'Cable Flyes', 'duration': '30 mins', 'reps': 6, 'sets': 5},
            {'name': 'Deadlift', 'duration': '30 mins', 'reps': 6, 'sets': 5},
            {'name': 'Barbell Squats', 'duration': '30 mins', 'reps': 6, 'sets': 5},
            {'name': 'Dumbbell Bench Press', 'duration': '30 mins', 'reps': 6, 'sets': 5},
        ],
        'without_equipment': [
            {'name': 'Burpees', 'duration': '25 mins', 'reps': 20, 'sets': 4},
            {'name': 'Pike Push-ups', 'duration': '25 mins', 'reps': 20, 'sets': 4},
            {'name': 'Handstand Push-ups', 'duration': '25 mins', 'reps': 10, 'sets': 4},
            {'name': 'Tuck Jumps', 'duration': '25 mins', 'reps': 15, 'sets': 4},
            {'name': 'Box Jumps', 'duration': '25 mins', 'reps': 15, 'sets': 4},
            {'name': 'Mountain Climbers', 'duration': '25 mins', 'reps': 20, 'sets': 4},
        ]
    },
    'extremely_active': {
        'with_equipment': [
            {'name': 'Snatch', 'duration': '45 mins', 'reps': 5, 'sets': 5},
            {'name': 'Front Squats', 'duration': '45 mins', 'reps': 5, 'sets': 5},
            {'name': 'Deadlifts', 'duration': '45 mins', 'reps': 5, 'sets': 5},
            {'name': 'Barbell Bench Press', 'duration': '45 mins', 'reps': 5, 'sets': 5},
            {'name': 'Leg Press', 'duration': '45 mins', 'reps': 10, 'sets': 5},
        ],
        'without_equipment': [
            {'name': 'One-Arm Push-ups', 'duration': '30 mins', 'reps': 10, 'sets': 5},
            {'name': 'Handstand Push-ups', 'duration': '30 mins', 'reps': 10, 'sets': 5},
            {'name': 'Burpees', 'duration': '30 mins', 'reps': 10, 'sets': 5},
            {'name': 'Dips', 'duration': '30 mins', 'reps': 8, 'sets': 5},
            {'name': 'plank jacks', 'duration': '30 mins', 'reps': 0, 'sets': 1},
        ]
    }
}

cardio_exercises = {
    'sedentary': {
        'with_equipment': [
            {'name': 'Stationary Bike', 'duration': '20 mins', 'reps': 1, 'sets': 1},
            {'name': 'Jogging', 'duration': '20 mins', 'reps': 1, 'sets': 1},
            {'name': 'Elliptical Trainer', 'duration': '20 mins', 'reps': 1, 'sets': 1},
            {'name': 'Rowing Machine', 'duration': '20 mins', 'reps': 1, 'sets': 1},
        ],
        'without_equipment': [
            {'name': 'Walking', 'duration': '30 mins', 'reps': 1, 'sets': 1},
            {'name': 'Jumping Jacks', 'duration': '10 mins', 'reps': 1, 'sets': 5},
            {'name': 'Bodyweight Squats', 'duration': '15 mins', 'reps': 10, 'sets': 3},
            {'name': 'High Knees', 'duration': '10 mins', 'reps': 1, 'sets': 5},
            {'name': 'Burpees', 'duration': '10 mins', 'reps': 1, 'sets': 5},
        ]
    },
    'lightly_active': {
        'with_equipment': [
            {'name': 'Treadmill Jog', 'duration': '30 mins', 'reps': 1, 'sets': 1},
            {'name': 'Stationary Rowing', 'duration': '20 mins', 'reps': 1, 'sets': 1},
            {'name': 'Recumbent Bike', 'duration': '30 mins', 'reps': 1, 'sets': 1},
            {'name': 'Stair Climber', 'duration': '20 mins', 'reps': 1, 'sets': 1},
            {'name': 'Circuit Training', 'duration': '30 mins', 'reps': 1, 'sets': 1},
        ],
        'without_equipment': [
            {'name': 'Light Jogging', 'duration': '30 mins', 'reps': 1, 'sets': 1},
            {'name': 'Brisk Walking', 'duration': '30 mins', 'reps': 1, 'sets': 1},
            {'name': 'Bodyweight Lunges', 'duration': '30 mins', 'reps': 1, 'sets': 1},
            {'name': 'Mountain Climbers', 'duration': '10 mins', 'reps': 0, 'sets': 5},
            {'name': 'Zumba', 'duration': '30 mins', 'reps': 0, 'sets': 0},
        ]
    },
    'moderately_active': {
        'with_equipment': [
            {'name': 'Elliptical', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'Stationary Bike', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'Rowing Machine', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'Stair Climber', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'Arc Trainer', 'duration': '45 mins', 'reps': 1, 'sets': 1},
        ],
        'without_equipment': [
            {'name': 'Running', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'Brisk Walking', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'Jump Rope', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'Hiking', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'jumping jacks', 'duration': '45 mins', 'reps': 1, 'sets': 1},
        ]
    },
    'very_active': {
        'with_equipment': [
            {'name': 'Rowing Machine', 'duration': '60 mins', 'reps': 1, 'sets': 1},
            {'name': 'Treadmill Sprints', 'duration': '60 mins', 'reps': 1, 'sets': 1},
            {'name': 'High-Intensity Interval Training (HIIT) on Stationary Bike', 'duration': '60 mins', 'reps': 1, 'sets': 1},
            {'name': 'Battle Ropes', 'duration': '60 mins', 'reps': 1, 'sets': 1},
            {'name': 'Kettlebell Swings', 'duration': '60 mins', 'reps': 1, 'sets': 1},
        ],
        'without_equipment': [
            {'name': 'Sprint Intervals', 'duration': '30 mins', 'reps': 1, 'sets': 1},
            {'name': 'Burpees', 'duration': '30 mins', 'reps': 0, 'sets': 0},
            {'name': 'Box Jumps', 'duration': '30 mins', 'reps': 1, 'sets': 1},
            {'name': 'Mountain Climbers', 'duration': '30 mins', 'reps': 1, 'sets': 1},
            {'name': 'Jump Squats', 'duration': '30 mins', 'reps': 1, 'sets': 1},
        ]
    },
    'extremely_active': {
        'with_equipment': [
            {'name': 'HIIT on Bike', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'Rowing Machine Intervals', 'duration': '30 mins', 'reps': 5, 'sets': 1},
            {'name': 'Stair Climber Sprints', 'duration': '30 mins', 'reps': 10, 'sets': 1},
            {'name': 'Battle Ropes', 'duration': '30 mins', 'reps': 10, 'sets': 1},
        ],
        'without_equipment': [
            {'name': 'HIIT Running', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'Burpees', 'duration': '20 mins', 'reps': 20, 'sets': 3},
            {'name': 'Mountain Climbers', 'duration': '15 mins', 'reps': 0, 'sets': 3},
        ]
    }
}

flexibility_exercises = {
    'sedentary': {
        'with_equipment': [
            {'name': 'Resistance Band Stretching', 'duration': '15 mins', 'reps': 1, 'sets': 1},
            {'name': 'Foam Roller Stretching', 'duration': '10 mins', 'reps': 1, 'sets': 1},
            {'name': 'Yoga Wheel Stretch', 'duration': '15 mins', 'reps': 1, 'sets': 1},
            {'name': 'Resistance Band Hamstring Stretch', 'duration': '15 mins', 'reps': 1, 'sets': 1},
            {'name': 'Stability Ball Back Stretch', 'duration': '15 mins', 'reps': 1, 'sets': 1},
            {'name': 'Dumbbell Overhead Tricep Stretch', 'duration': '5 mins', 'reps': 2, 'sets': 1},
        ],
        'without_equipment': [
            {'name': 'Basic Yoga', 'duration': '20 mins', 'reps': 1, 'sets': 1},
            {'name': 'Seated Forward Bend', 'duration': '5 mins', 'reps': 2, 'sets': 1},
            {'name': 'Cat-Cow Stretch', 'duration': '5 mins', 'reps': 10, 'sets': 1},
            {'name': 'Standing Quadriceps Stretch', 'duration': '5 mins', 'reps': 2, 'sets': 1},
            {'name': 'Lying Spinal Twist', 'duration': '5 mins', 'reps': 2, 'sets': 1},
        ]
    },
    'lightly_active': {
        'with_equipment': [
            {'name': 'Foam Rolling', 'duration': '20 mins', 'reps': 1, 'sets': 1},
            {'name': 'Resistance Band Shoulder Stretch', 'duration': '10 mins', 'reps': 2, 'sets': 1},
            {'name': 'Weighted Hip Flexor Stretch', 'duration': '15 mins', 'reps': 2, 'sets': 1},
            {'name': 'Cable Machine Chest Stretch', 'duration': '10 mins', 'reps': 2, 'sets': 1},
            {'name': 'TRX Hamstring Stretch', 'duration': '10 mins', 'reps': 2, 'sets': 1},
        ],
        'without_equipment': [
            {'name': 'Intermediate Yoga', 'duration': '30 mins', 'reps': 1, 'sets': 1},
            {'name': 'Pigeon Pose', 'duration': '5 mins', 'reps': 0, 'sets': 0},
            {'name': 'Lizard Pose', 'duration': '5 mins', 'reps': 0, 'sets': 0},
            {'name': 'Cobra Stretch', 'duration': '5 mins', 'reps': 0, 'sets': 0},
            {'name': 'Seated Straddle Stretch', 'duration': '5 mins', 'reps': 0, 'sets': 0},
        ]
    },
    'moderately_active': {
        'with_equipment': [
            {'name': 'Dynamic Stretching', 'duration': '25 mins', 'reps': 1, 'sets': 1},
            {'name': 'Foam Roller Stretching', 'duration': '20 mins', 'reps': 1, 'sets': 1},
            {'name': 'Resistance Band Hamstring Stretch', 'duration': '15 mins', 'reps': 3, 'sets': 1},
            {'name': 'Stability Ball Back Stretch', 'duration': '10 mins', 'reps': 5, 'sets': 1},
        ],
        'without_equipment': [
            {'name': 'Advanced Yoga', 'duration': '40 mins', 'reps': 1, 'sets': 1},
            {'name': 'Standing Quadriceps Stretch', 'duration': '10 mins', 'reps': 3, 'sets': 1},
            {'name': 'Seated Forward Bend', 'duration': '15 mins', 'reps': 1, 'sets': 1},
            {'name': 'Cat-Cow Stretch', 'duration': '10 mins', 'reps': 10, 'sets': 1},
            {'name': 'Lying Spinal Twist', 'duration': '10 mins', 'reps': 3, 'sets': 1},
        ]
    },
    'very_active': {
        'with_equipment': [
            {'name': 'Pilates with Equipment', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'Foam Roller IT Band Stretch', 'duration': '15 mins', 'reps': 1, 'sets': 1},
            {'name': 'Cable Chest Stretch', 'duration': '10 mins', 'reps': 3, 'sets': 1},
            {'name': 'Resistance Band Shoulder Stretch', 'duration': '10 mins', 'reps': 3, 'sets': 1},
            {'name': 'Yoga Wheel Backbend', 'duration': '15 mins', 'reps': 5, 'sets': 1},
            {'name': 'Weighted Hip Flexor Stretch', 'duration': '10 mins', 'reps': 3, 'sets': 1},
        ],
        'without_equipment': [
            {'name': 'Pilates', 'duration': '45 mins', 'reps': 1, 'sets': 1},
            {'name': 'Dynamic Lunge with Twist', 'duration': '10 mins', 'reps': 10, 'sets': 2},
            {'name': 'Pigeon Pose', 'duration': '10 mins', 'reps': 1, 'sets': 2},
            {'name': 'Bridge Pose', 'duration': '10 mins', 'reps': 1, 'sets': 2},
            {'name': 'Standing Forward Bend', 'duration': '10 mins', 'reps': 1, 'sets': 2},
        ]
    },
    'extremely_active': {
        'with_equipment': [
            {'name': 'Extreme Stretching', 'duration': '60 mins', 'reps': 1, 'sets': 1},
            {'name': 'Foam Roller Stretching', 'duration': '30 mins', 'reps': 1, 'sets': 1},
            {'name': 'Resistance Band Hamstring Stretch', 'duration': '15 mins', 'reps': 3, 'sets': 2},
            {'name': 'Weighted Forward Bend', 'duration': '20 mins', 'reps': 10, 'sets': 2},
        ],
        'without_equipment': [
            {'name': 'Power Yoga', 'duration': '60 mins', 'reps': 1, 'sets': 1},
            {'name': 'Dynamic Leg Swings', 'duration': '10 mins', 'reps': 10, 'sets': 2},
            {'name': 'Seated Straddle Stretch', 'duration': '15 mins', 'reps': 1, 'sets': 2},
            {'name': 'Cat-Cow Stretch', 'duration': '10 mins', 'reps': 10, 'sets': 2},
            {'name': 'Power Yoga', 'duration': '60 mins', 'reps': 1, 'sets': 1},
        ]
    }
}
