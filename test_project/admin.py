from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

# Register your models here.
admin.site.unregister(User)

class Cromo_RepInline(admin.StackedInline):
	model=Cromo_Rep
	extra=1

class CromoAdmin(admin.ModelAdmin):
	inlines=[Cromo_RepInline]

class UserProfileInline(admin.StackedInline):
	model= UserProfile
	list_display=('cromo_id','repetido')

class CustomUserAdmin(UserAdmin):
	save_on_top=True
	list_display=('username','email','first_name','last_name','is_staff','last_login')
	inlines=[UserProfileInline]
admin.site.register(User,CustomUserAdmin)
admin.site.register(Pagina)
admin.site.register(Cromo,CromoAdmin)
admin.site.register(Estadistica)
admin.site.register(List_Cromo)
admin.site.register(Cromo_Rep,)