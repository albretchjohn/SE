from django.urls import path
from .views import register_user, home, contact, user_login, logout_view, resources, about, verify_otp, user_dashboard, profiling, faculty_dashboard, the_admin, generate_plan, display_plan, view_exercise_plans, register_faculty, dashboard_faculty_test, user_detail, csspe_dashboard, he_dashboard, resend_otp, user_view_details, user_view_details_d, exercise_data_view, facultyLog, dashboard_view
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('register/', register_user, name='register_user'),
    path('resend-otp/', resend_otp, name='resend_otp'),
    path('verify/', verify_otp, name='verify_otp'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('resources/', resources, name='resources'),
    path('login/', user_login, name='user_login'),
    path('Dashboard/', user_dashboard, name='user_dashboard'),
    path('Profiling/', profiling, name='profiling'),
    path('Facultyd/', faculty_dashboard, name='faculty_dashboard'),
    path('admin-dashboard/', the_admin, name='admin_interface'),
    path('logout/', logout_view, name='logout'),
    path('generate/', generate_plan, name='generate_plan'),
    path('Plan', display_plan, name='display_plan'),
    path('sample/', view_exercise_plans, name='view_exercise_plans'),
    path('faculty-register/', register_faculty, name='faculty_register'),
    path('f-dash-test/',dashboard_faculty_test, name='dashboard_faculty_test'),
    path('user_detail/<int:user_id>/', user_detail, name='user_detail'),
    path('csspe/', csspe_dashboard, name='csspe_dashboard'),
    path('he/', he_dashboard, name='he_dashboard'),
    path('View-Details/<int:user_id>/',user_view_details, name='user_view_details'),
    path('User-View-Details-d/<int:user_id>/',user_view_details_d, name='user_view_details_d'),
    path('submit-progress/', views.submit_progress, name='submit_progress'), 
    path('exercise-data/', exercise_data_view, name='exerciseList'),
    path('faculty-log/<int:id>/', facultyLog, name='facultyLog'),
    path('adminDashboard/', dashboard_view, name='adminDashboard'),
]