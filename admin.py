from django.contrib import admin
from .models import Job,Donation
from .models import College,Course,Alumni,Review

admin.site.register(College)
admin.site.register(Course)


class AlumniAdmin(admin.ModelAdmin):
    # List fields to display in the admin (excluding 'user')
    list_display = ('name', 'email', 'phonenumber', 'college', 'course', 'year_of_passout')

admin.site.register(Alumni, AlumniAdmin)



admin.site.register(Job)
admin.site.register(Donation)
admin.site.register(Review)


# Register your models here.
