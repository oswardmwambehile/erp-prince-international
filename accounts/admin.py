from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Company,
    Branch,
    Department,
    Position,
    User
)


# ===================================
# COMPANY ADMIN
# ===================================
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'code',
        'email',
        'phone',
        'is_active',
        'created_at'
    )

    search_fields = (
        'name',
        'code',
        'email'
    )

    list_filter = (
        'is_active',
        'created_at'
    )

    ordering = ('name',)


# ===================================
# BRANCH ADMIN
# ===================================
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'company',
        'code',
        'location',
        'is_active'
    )

    search_fields = (
        'name',
        'code',
        'location'
    )

    list_filter = (
        'company',
        'is_active'
    )

    ordering = ('name',)


# ===================================
# DEPARTMENT ADMIN
# ===================================
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'company',
        'code',
        'is_active',
        'created_at'
    )

    search_fields = (
        'name',
        'code'
    )

    list_filter = (
        'company',
        'is_active'
    )

    ordering = ('name',)


# ===================================
# POSITION ADMIN
# ===================================
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'company',
        'is_active',
        'created_at'
    )

    search_fields = (
        'name',
    )

    list_filter = (
        'company',
        'is_active'
    )

    ordering = ('name',)


# ===================================
# CUSTOM USER ADMIN
# ===================================
@admin.register(User)
class CustomUserAdmin(UserAdmin):

    model = User

    list_display = (
        'email',
        'first_name',
        'last_name',
        'company',
        'branch',
        'department',
        'position',
        'is_staff',
        'is_active'
    )

    list_filter = (
        'company',
        'branch',
        'department',
        'position',
        'is_staff',
        'is_active'
    )

    search_fields = (
        'email',
        'first_name',
        'last_name',
        'contact'
    )

    ordering = ('email',)

    readonly_fields = (
        'date_joined',
        'updated_at'
    )

    fieldsets = (

        ('Login Credentials', {
            'fields': (
                'email',
                'password'
            )
        }),

        ('Personal Information', {
            'fields': (
                'first_name',
                'last_name',
                'contact'
            )
        }),

        ('Company Information', {
            'fields': (
                'company',
                'branch',
                'department',
                'position'
            )
        }),

        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),

        ('Important Dates', {
            'fields': (
                'last_login',
                'date_joined',
                'updated_at'
            )
        }),
    )

    add_fieldsets = (

        (None, {
            'classes': ('wide',),

            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'contact',
                'company',
                'branch',
                'department',
                'position',
                'is_staff',
                'is_active'
            ),
        }),
    )