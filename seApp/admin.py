from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser, OTP, Profile, DietPlan, ExercisePlan, Faculty, E_PlanApproval, D_PlanApproval


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('user_type',)}),
    )
    list_display = ('username', 'email', 'user_type', 'is_active', 'date_joined')
    list_filter = ('user_type', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

admin.site.unregister(Group)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp_code', 'created_at', 'expires_at')
    search_fields = ('user__username', 'otp_code')
    list_filter = ('created_at', 'expires_at')

class CommonInfoAdmin(admin.ModelAdmin): 
    search_fields = ('user__username',) 
    list_filter = ('date_created', 'status')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'college_department', 'birthday', 'gender')
    search_fields = ('user__username', 'first_name', 'last_name', 'college_department')
    list_filter = ('college_department', 'gender', 'body_type', 'activity_level')

@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'calorie_intake_per_day', 'date_created', 'status')
    list_filter = ('status', 'date_created')
    search_fields = ('user__username',)
    date_hierarchy = 'date_created'


@admin.register(ExercisePlan)
class ExercisePlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_created', 'status')
    list_filter = ('status', 'date_created')
    search_fields = ('user__username',)
    date_hierarchy = 'date_created'

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    search_fields = ('name', 'email', 'department')
    list_filter = ('department',)

@admin.register(E_PlanApproval)
class PlanApprovalAdmin(admin.ModelAdmin):
    list_display = ('E_plan', 'faculty', 'status', 'review_date')
    search_fields = ('plan__user__username', 'faculty__name')
    list_filter = ('status', 'review_date')
    ordering = ('-review_date',)

@admin.register(D_PlanApproval)
class PlanApprovalAdmin(admin.ModelAdmin):
    list_display = ('D_plan', 'faculty', 'status', 'review_date')
    search_fields = ('plan__user__username', 'faculty__name')
    list_filter = ('status', 'review_date')
    ordering = ('-review_date',)

