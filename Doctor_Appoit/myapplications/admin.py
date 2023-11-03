from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Doctor, Schedule, Contact, Appointment


# Register your models here.


admin.site.site_header = 'Online Doctors Appointment'
admin.site.site_title = 'Administration'
admin.site.index_title = 'Online Doctors Appointment'
admin.site.unregister(Group)


@admin.register(Doctor)
class AdminDoctor(admin.ModelAdmin):
    list_display = ['d_id', 'd_name', 'd_mobile', 'd_qualification', 'd_specialist', 'd_yoe']


@admin.register(Schedule)
class AdminSchedule(admin.ModelAdmin):
    list_display = ['doctors', 'days', 'time_slot']
    raw_id_fields = ["doctor"]

    def doctors(self, obj):
        return obj.doctor.d_name


admin.site.register(Contact)


@admin.register(Appointment)
class AdminAppointment(admin.ModelAdmin):
    list_display = ['patients', 'doctors', 'app_made_on', 'app_fix_date']

    def doctors(self, obj):
        return obj.doctor.d_name

    def patients(self, obj):
        return obj.user.first_name+" "+obj.user.last_name
