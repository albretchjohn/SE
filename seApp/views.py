from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import send_mail
from .models import OTP, CustomUser, Profile, DietPlan, ExercisePlan, Faculty, E_PlanApproval, D_PlanApproval, WeightEntry
from django.utils import timezone
from datetime import datetime
from .exercise_data import strength_exercises, cardio_exercises, flexibility_exercises 
import random
from django.db.models import Q
from django.core.paginator import Paginator

# User = get_user_model()

#to home/landing page
def home (request):
    return render (request, 'home.html')

#no content yet
def resources (request):
    return render (request, 'resources.html')

#no content yet
def about (request):
    return render (request, 'about.html')

#no content yet
def contact (request):
    return render (request, 'contact.html')

# sends otp to email for wellnes users only
def send_otp_email(user, otp_code):
    send_mail(
        'Your OTP Code',
        f'Your OTP code is {otp_code}',
        'fharhanasali19@gmail.com',
        [user.email],
        fail_silently=False,
    )

#resends otp if expires
def resend_otp(request):
    if request.method == 'POST':
        username = request.POST['username']

        try:
            user = CustomUser.objects.get(username=username)
            otp = OTP.objects.filter(user=user).first()

            if otp:
                otp.otp_code = str(random.randint(100000, 999999))
                otp.expires_at = timezone.now() + timezone.timedelta(minutes=10)
                otp.save()

                send_mail(
                    'Your Resent OTP Code',
                    f'Your new OTP code is {otp.otp_code}',
                    'fharhanasali19@gmailexample.com',
                    [user.email],
                    fail_silently=False,
                )

                messages.success(request, 'A new OTP has been sent to your email.')
            else:
                messages.error(request, 'No OTP found for this user.')

        except CustomUser.DoesNotExist:
            messages.error(request, 'User not found.')

        return redirect('verify_otp')

    return render(request, 'resend_otp.html')

#registering wellness users
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = CustomUser.objects.create_user(username=username, email=email, password=password, user_type='user')
        user.is_active = False
        user.save()

        otp_code = str(random.randint(100000, 999999))
        OTP.objects.create(user=user, otp_code=otp_code, expires_at=timezone.now() + timezone.timedelta(minutes=10))

        send_otp_email(user, otp_code)

        messages.success(request, 'User registered successfully. Please check your email for the OTP code.')
        return redirect('verify_otp')

    return render(request, 'register_user.html')

#only admin has access/registers faculty members
# @login_required
# @user_passes_test(lambda u: u.user_type == 'Admin')
# def register_faculty(request):
#     if request.user.user_type != 'Admin': 
#         messages.error(request, 'You do not have permission to register a faculty member.')
#         return redirect('home')
    
#     if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         department = request.POST['department']

#         user = CustomUser.objects.create_user(
#             username=username, 
#             first_name=first_name, 
#             last_name=last_name, 
#             email=email, 
#             password=password, 
#             user_type='faculty',
#             is_staff=True
#         )
#         user.is_active = True
#         user.save()
        
#         Faculty.objects.create(name=f"{first_name} {last_name}", email=email, department=department)

#         messages.success(request, 'Faculty registered successfully.')
#         return redirect('admin_interface')

#     return render(request, 'faculty_register.html')

# @login_required
def register_faculty(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        department = request.POST['department']

        user = CustomUser.objects.create_user(
            username=username, 
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            password=password, 
            user_type='faculty',
            is_staff=True
        )
        user.is_active = True
        user.save()
        
        Faculty.objects.create(name=f"{first_name} {last_name}", email=email, department=department)

        messages.success(request, 'Faculty registered successfully.')
        # return redirect('admin_interface')
        return redirect('home')

    return render(request, 'faculty_register.html')

#authenticate if otp is correct
def verify_otp(request):
    if request.method == 'POST':
        otp_code = request.POST['otp_code']
        username = request.POST['username']
        
        try:
            user = CustomUser.objects.get(username=username)
            otp = OTP.objects.get(user=user, otp_code=otp_code)

            if otp.expires_at < timezone.now():
                messages.error(request, 'OTP has expired.')
                return redirect('verify_otp')

            user.is_active = True
            user.save()
            otp.delete()

            messages.success(request, 'OTP verified successfully. Your account is now active.')
            return redirect('user_login')
        except (CustomUser.DoesNotExist, OTP.DoesNotExist):
            messages.error(request, 'Invalid OTP or username.')
            return redirect('verify_otp')

    return render(request, 'verify_otp.html')

#interface for logging in for all users
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return handle_user_redirect(request, user)
        else:
            messages.error(request, 'Invalid username or password')
            # return redirect('user_login')

    return render(request, 'user_login.html')

#function connected for logging in
def handle_user_redirect(request, user):
    try:
        if user.user_type == 'user':
            if Profile.objects.filter(user=user).exists():
                return redirect('user_dashboard')
            else:
                return redirect('profiling')
        elif user.user_type == 'faculty':
            faculty = get_object_or_404(Faculty, email=user.email)
            department = faculty.department.lower()
            if department in ['csspe', 'college of sports science and physical education']:
                return redirect('csspe_dashboard')
            else:
                return redirect('he_dashboard')
        elif user.user_type.lower() == 'admin':
            return redirect('admin_interface')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
        return redirect('user_login')

# interface for ccspe members
@login_required
def csspe_dashboard(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        users = Profile.objects.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    else:
        # Show all users by default when loading the page
        users = Profile.objects.all()
        
    return render(request, 'csspe_dashboard.html', {'users': users})

    # return render(request, 'csspe_dashboard.html', {'users': []})


# interface for he members
@login_required
def he_dashboard(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        users = Profile.objects.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    else:
        users = Profile.objects.all()
    
    
    return render(request, 'he_dashboard.html', {'users': users})
    #  return render(request, 'he_dashboard.html', {'users': []})

#after registering wellness user/ function for getting their info
def profiling(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_initial = request.POST.get('middle_initial', '')
        college_department = request.POST['college_department']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        height = request.POST['height']
        weight = request.POST['weight']
        body_type = request.POST['body_type']
        activity_level = request.POST['activity_level']
        equipment_access = request.POST['equipment_access']
        medical_conditions = request.POST.getlist('medical_conditions') 
        other_condition = request.POST.get('other_condition', '')
        allergies = request.POST['allergies']
        allergy_details = request.POST.get('allergy_details_input', '')
        injuries = request.POST['injuries']

        if 'others' in medical_conditions and other_condition: 
            medical_conditions.append(other_condition)

        height_m = float(height) / 100
        weight_kg = float(weight)

        bmi = round(weight_kg / (height_m ** 2))

        profile = Profile.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            middle_initial=middle_initial,
            college_department=college_department,
            birthday=birthday,
            gender=gender,
            height=height,
            weight=weight,
            bmi=bmi,
            body_type=body_type,
            activity_level=activity_level,
            equipment_access=equipment_access,
            health_condition=', '.join(medical_conditions),
            allergies=allergy_details if allergies == 'yes' else 'No',
            injuries=injuries,
        )
        profile.save()
        messages.success(request, 'Profile created successfully.')
        return redirect('generate_plan')

    return render(request, 'user_profiling.html')

#calculate Basal Metabolic Rate
def calculate_bmr(profile):
    try:
        if profile.gender == 'M':
            bmr = 10 * profile.weight + 6.25 * profile.height - 5 * (timezone.now().year - profile.birthday.year) + 5
        else:
            bmr = 10 * profile.weight + 6.25 * profile.height - 5 * (timezone.now().year - profile.birthday.year) - 161
        return bmr
    except Exception as e:
        print(f"Error calculating BMR: {e}")
        return None
    
# computes diet plan
def generate_diet_plan(profile):
    try:
        bmr = calculate_bmr(profile)
        if bmr is None:
            return None

        activity_factors = {
            'sedentary': 1.2,
            'lightly_active': 1.375,
            'moderately_active': 1.55,
            'very_active': 1.725,
            'extremely_active': 1.9
        }
        tdee = bmr * activity_factors.get(profile.activity_level, 1.2)
        
        calorie_intake_per_day = round(tdee - 500, 2)
        protein_calories = round(calorie_intake_per_day * 0.25, 2)
        carb_calories = round(calorie_intake_per_day * 0.5, 2)
        fat_calories = round(calorie_intake_per_day * 0.25, 2)

        protein_per_meal = round(protein_calories / 4 / 3, 2)
        carb_per_meal = round(carb_calories / 4 / 3, 2)
        fat_per_meal = round(fat_calories / 9 / 3, 2)

        return {
            'user_id': profile.user.id,
            'calorie_intake_per_day': calorie_intake_per_day,
            'fats_per_meal': fat_per_meal,
            'carbs_per_meal': carb_per_meal,
            'protein_per_meal': protein_per_meal,
            'status': 'Pending'
        }
    except Exception as e:
        print(f"Error generating diet plan: {e}")
        return None
    
#makes exercise routine/ list of exercise in 'exercise_data.py'
def generate_exercise_routine(profile):
    try:
        activity_level = 'sedentary' if profile.health_condition.count(',') >= 2 else profile.activity_level
        equipment = 'with_equipment' if 'yes' in profile.equipment_access.lower() else 'without_equipment'

        def select_exercises(exercises, num_exercises=3):
            return random.sample(exercises, k=random.randint(2, num_exercises))

        strength_routine = select_exercises(strength_exercises[activity_level][equipment])
        cardio_routine = select_exercises(cardio_exercises[activity_level][equipment])
        flexibility_routine = select_exercises(flexibility_exercises[activity_level][equipment])

        weekly_routine = {
            'day_1': strength_routine,
            'day_2': cardio_routine,
            'day_3': strength_routine,
            'day_4': flexibility_routine,
            'day_5': cardio_routine,
            'day_6': strength_routine,
            'day_7': [{'name': 'Rest Day', 'duration': '0 mins', 'reps': 0, 'sets': 0}]
        }

        return {
            'user_id': profile.user.id,
            'strength_exercises': ', '.join([ex['name'] for ex in strength_routine]),
            'flexibility_exercises': ', '.join([ex['name'] for ex in flexibility_routine]),
            'cardio_exercises': ', '.join([ex['name'] for ex in cardio_routine]),
            'routine': weekly_routine,
            'rest_day': 'Sunday',
            'status': 'Pending'
        }
    except Exception as e:
        print(f"Error generating exercise routine: {e}")
        return None

# calls those two functions to generate plan
@login_required
def generate_plan(request):
    try:
        profile = Profile.objects.get(user=request.user)

        diet_plan_data = generate_diet_plan(profile)
        exercise_plan_data = generate_exercise_routine(profile)

        if diet_plan_data and exercise_plan_data:
            request.session['diet_plan'] = diet_plan_data
            request.session['exercise_plan'] = exercise_plan_data
            return redirect('display_plan')
        else:
            messages.error(request, 'Error generating plans. Please try again.')
            return redirect('profiling')
    except Profile.DoesNotExist:
        messages.error(request, 'Profile not found.')
        return redirect('profiling')

#let's user see the plan before saving to database
@login_required
def display_plan(request):
    diet_plan = request.session.get('diet_plan')
    exercise_plan = request.session.get('exercise_plan')

    if not diet_plan or not exercise_plan:
        messages.error(request, 'Error retrieving plans. Please generate your plans again.')
        return redirect('generate_plan')

    if request.method == 'POST':
        try:
            diet_plan_instance = DietPlan(
                user_id=diet_plan['user_id'],
                calorie_intake_per_day=diet_plan['calorie_intake_per_day'],
                fats_per_meal=diet_plan['fats_per_meal'],
                carbs_per_meal=diet_plan['carbs_per_meal'],
                protein_per_meal=diet_plan['protein_per_meal'],
                status=diet_plan['status']
            )
            diet_plan_instance.save()

            exercise_plan_instance = ExercisePlan(
                user_id=exercise_plan['user_id'],
                strength_exercises=exercise_plan['strength_exercises'],
                flexibility_exercises=exercise_plan['flexibility_exercises'],
                cardio_exercises=exercise_plan['cardio_exercises'],
                routine=exercise_plan['routine'],
                rest_day=exercise_plan['rest_day'],
                status=exercise_plan['status']
            )
            exercise_plan_instance.save()

            messages.success(request, 'Plans saved successfully.')
            return redirect('user_dashboard')
        except Exception as e:
            messages.error(request, f'Error saving plans: {e}')
            return redirect('display_plan')

    return render(request, 'display_plan.html', {
        'diet_plan': diet_plan,
        'exercise_plan': exercise_plan
    })

# interface fo wellness users
@login_required
def user_dashboard(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
        
        diet_plan = DietPlan.objects.filter(user=request.user, status='Approved').first()
        exercise_plan = ExercisePlan.objects.filter(user=request.user, status='Approved').first()
        
        weight_entries = WeightEntry.objects.filter(user=request.user).order_by("-date_logged") #comments to ng user
        
        
        chart_entries = WeightEntry.objects.filter(user=request.user).order_by("date_logged")
        dates = [entry.date_logged.strftime("%Y-%m-%d") for entry in chart_entries]
        weights = [entry.weight for entry in chart_entries]
        
        current_bmi = None
        current_bmi_category = None
        if weight_entries and user_profile.height:
            current_weight = weight_entries[0].weight
            height_m = user_profile.height / 100  # convert cm to meters
            if height_m > 0:
                current_bmi = round(current_weight / (height_m ** 2), 2)
                
                if current_bmi < 18.5:
                    current_bmi_category = "Underweight"
                elif 18.5 <= current_bmi < 25:
                    current_bmi_category = "Normal"
                elif 25 <= current_bmi < 30:
                    current_bmi_category = "Overweight"
                else:
                    current_bmi_category = "Obese"                        
        
        dietitianComment = None
        if diet_plan:
            dietitianComment = D_PlanApproval.objects.filter(D_plan=diet_plan).order_by("-review_date").first()
            
        trainerComment = None
        if exercise_plan:
            trainerComment = E_PlanApproval.objects.filter(E_plan=exercise_plan).order_by("-review_date").first()

        if diet_plan and exercise_plan:
            return render(request, 'user_dashboard.html', {
                'user_profile': user_profile,
                'diet_plan': diet_plan,
                'exercise_plan': exercise_plan,
                'weights': weights,
                'dates': dates,
                'comments': weight_entries,
                'dietitianComment': dietitianComment,
                'trainerComment': trainerComment,
                'current_bmi': current_bmi,
                'current_bmi_category': current_bmi_category,
            })
        else:
            messages.info(request, 'Your personalized plans are still under review. Please come again later.')

        return render(request, 'user_dashboard.html', {
            'user_profile': user_profile,
            'diet_plan': diet_plan,
            'exercise_plan': exercise_plan,
            
        })
    except Profile.DoesNotExist:
        messages.error(request, 'Profile not found.')
        return redirect('profiling')



#after logging out
def logout_view(request):
     logout(request) 
     return redirect('home')

#for testing
def faculty_dashboard(request):
    return render (request, 'faculty_dashboard.html')

#for testing
def dashboard_faculty_test(request):
    query = request.GET.get('query', '')
    profiles = Profile.objects.filter(first_name__icontains=query) | Profile.objects.filter(last_name__icontains=query)
    return render(request, 'dashboard_faculty_test.html', {'profiles': profiles})

#for testing
def user_detail(request, user_id):
    profile = get_object_or_404(Profile, user__id=user_id)
    diet_plan = DietPlan.objects.filter(user__id=user_id).last()
    exercise_plan = ExercisePlan.objects.filter(user__id=user_id).last()
    context = {
        'profile': profile,
        'diet_plan': diet_plan,
        'exercise_plan': exercise_plan
    }
    return render(request, 'user_detail.html', context)

#admin interface 
# @login_required
def the_admin(request):
    query = request.GET.get('search', '').strip()
    faculty_list = Faculty.objects.all()

    
    if query:
        faculty_list = faculty_list.filter(name__icontains=query)
    if request.user.user_type.lower() != 'admin': 
         messages.error(request, 'You do not have permission to view this page.')
         return redirect('home')
     
    paginator = Paginator(faculty_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    context = {
        'faculty_list': faculty_list,
        'page_obj': page_obj,
    }
    return render(request, 'admin_interface.html', context)

#for testing
def view_exercise_plans(request):
     
      exercise_plans = ExercisePlan.objects.all() 
      return render(request, 'sample.html', {'exercise_plans': exercise_plans})

#function for  csspe faculty to do CRUD
@login_required
def user_view_details(request, user_id):
    # approved_by = f"{request.user.first_name} {request.user.last_name}"
    
    user_profile = get_object_or_404(Profile, user_id=user_id)
    exercise_plan = get_object_or_404(ExercisePlan, user_id=user_id)
    diet_plan = DietPlan.objects.filter(user_id=user_id, status='Approved').first()
    
    user = user_profile.user
    comments = WeightEntry.objects.filter(user=user).order_by("-date_logged")
    
    chart_entries = WeightEntry.objects.filter(user=user).order_by("date_logged")
    dates = [entry.date_logged.strftime("%Y-%m-%d") for entry in chart_entries]
    weights = [entry.weight for entry in chart_entries]
    

    if request.method == 'POST':
        try:
            exercise_plan.strength_exercises = request.POST.get('strength_exercises', exercise_plan.strength_exercises)
            exercise_plan.flexibility_exercises = request.POST.get('flexibility_exercises', exercise_plan.flexibility_exercises)
            exercise_plan.cardio_exercises = request.POST.get('cardio_exercises', exercise_plan.cardio_exercises)
            # exercise_plan.routine = request.POST.get('routine', exercise_plan.routine)
            routine_dict = {}
            for day in range(1, 8):
                exercises = []
                i = 0
                while True:
                    name = request.POST.get(f'routine[day_{day}][{i}][name]')
                    duration = request.POST.get(f'routine[day_{day}][{i}][duration]')
                    reps = request.POST.get(f'routine[day_{day}][{i}][reps]')
                    sets = request.POST.get(f'routine[day_{day}][{i}][sets]')
                    if not name:
                        break
                    exercises.append({
                        'name': name,
                        'duration': duration or '',
                        'reps': reps or '',
                        'sets': sets or '',
                    })
                    i += 1
                routine_dict[f'day_{day}'] = exercises
            
            exercise_plan.routine = routine_dict
            exercise_plan.rest_day = request.POST.get('rest_day', exercise_plan.rest_day)
            exercise_plan.status = request.POST.get('status', exercise_plan.status)
            exercise_plan.reviewed_by_fullname_csspe = request.user.get_full_name()
            exercise_plan.save()

            faculty = Faculty.objects.get(email=request.user.email)
            E_PlanApproval.objects.create(
                E_plan=exercise_plan,
                faculty=faculty,
                status=request.POST.get('status', exercise_plan.status),
                review_comments=request.POST.get('review_comments', '')
            )

            messages.success(request, 'Exercise plan updated successfully.')
            return redirect('csspe_dashboard')
        except Exception as e:
            messages.error(request, f"Error saving exercise plan: {e}")
            return redirect('user_view_details', user_id=user_id)

    return render(request, 'user_view_details.html', {
        'user_profile': user_profile,
        'exercise_plan': exercise_plan,
        'diet_plan': diet_plan,
        'approved_by': exercise_plan.reviewed_by_fullname_csspe,
        'comments': comments,
        'dates': dates,
        'weights': weights,
        
    })


#function for  he faculty to do CRUD on user
@login_required
def user_view_details_d(request, user_id):
    user_profile = get_object_or_404(Profile, user_id=user_id)
    diet_plan = get_object_or_404(DietPlan, user_id=user_id)
    
    user = user_profile.user
    comments = WeightEntry.objects.filter(user=user).order_by("-date_logged")
    # dietitianComment = D_PlanApproval.objects.filter(D_plan__user=user).order_by("-review_date").first()
    
    chart_entries = WeightEntry.objects.filter(user=user).order_by("date_logged")
    dates = [entry.date_logged.strftime("%Y-%m-%d") for entry in chart_entries]
    weights = [entry.weight for entry in chart_entries]
    

    if request.method == 'POST':
        diet_plan.calorie_intake_per_day = request.POST['calorie_intake_per_day']
        diet_plan.carbs_per_meal = request.POST['carbs_per_meal']
        diet_plan.fats_per_meal = request.POST['fats_per_meal']
        diet_plan.protein_per_meal = request.POST['protein_per_meal']
        diet_plan.status = request.POST['status']
        diet_plan.reviewed_by_fullname_he = request.user.get_full_name()
        diet_plan.save()

        faculty = Faculty.objects.get(email=request.user.email)
        D_PlanApproval.objects.create(
            D_plan =diet_plan,
            faculty=faculty,
            status=request.POST['status'],
            review_comments=request.POST['review_comments']
        )

        messages.success(request, 'Diet plan updated successfully.')
        return redirect('he_dashboard')

    return render(request, 'user_view_details_d.html', {
        'user_profile': user_profile,
        'diet_plan': diet_plan,
        'approved_by': diet_plan.reviewed_by_fullname_he,
        'comments': comments,
        'dates': dates,
        'weights': weights,
        # 'dietitianComment': dietitianComment
    })
    
@login_required
def submit_progress(request):
    if request.method == "POST":
        weight = request.POST.get('current_weight')
        comment = request.POST.get('comments')

        if weight:
            WeightEntry.objects.create(
                user=request.user,
                weight=weight,
                comment=comment
            )
        return redirect('user_dashboard')  # or wherever you want to redirect after saving

    return redirect('user_dashboard')  # fallback if accessed via GET


def exercise_data_view(request):
    context = {
        'strength_exercises': strength_exercises,
        'cardio_exercises': cardio_exercises,
        'flexibility_exercises': flexibility_exercises,
    }
    return render(request, 'exerciseList.html', context)





