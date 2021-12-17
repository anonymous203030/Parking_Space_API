from django.contrib import admin

# Register your models here.
from .models import User, UserProfile


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'profession', 'created_at', 'updated_at',)
    list_filter = ('is_staff', 'created_at', 'updated_at',)
    ordering = ('created_at',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'profession')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email',)


admin.site.register(User, UsersAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday', 'gender', 'owner', 'image', 'created_at', 'about')
    list_filter = ('birthday', 'gender', 'owner')
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name', 'about')

    fieldsets = [
        ("Worker", {'fields': ['owner'],
                    'classes': ['collapse']}),
        ('About worker', {'fields': (('first_name', 'last_name'), ('birthday', 'gender'), 'image', 'about'),
                          'classes': ['collapse']}),
    ]


admin.site.register(UserProfile, UserProfileAdmin)
