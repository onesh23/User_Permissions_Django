from django.contrib import admin
from new_app.models import User, VehicleModel

# Register your models here.

admin.site.register(User)


class ReadOnlyAdminMixin:
    def has_add_permission(self,request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_admin:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_admin or request.user.is_user:
            return True 
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

@admin.register(VehicleModel)
class VehicleAdmin(ReadOnlyAdminMixin,admin.ModelAdmin):
    list_display = ['vehicle_number','Vehicle_type','vehicle_model']
