from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from django.contrib.auth.models import User

from .forms import UserChangeForm, UserCreationForm
from .models import Usuario, UserProfile


@admin.register(Usuario)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Usuario
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields": ("bio",)}),
    )

class UserProfileAdmin(admin.ModelAdmin):
    model: UserProfile
    list_display = ['user', 'telefone', 'endereço_completo', 'nome_completo','funçao']
    search_fields = ['user']
    list_filter = ['user']
    save_on_top = True

admin.site.register(UserProfile, UserProfileAdmin)