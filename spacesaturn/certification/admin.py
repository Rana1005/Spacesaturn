from django.contrib import admin

# Register your models here.
admin.site.site_header = 'Krishanujeet Panel'


# from django.contrib import admin
from .models import CandidateCertificate

class CandidateCertificateAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = (
        'name', 'space_id', 'certificate_id', 'father_name', 'mother_name', 
        'cs_fundamental_window', 'ms_word', 'ms_excel', 'ms_powerpoint', 'ms_outlook_internet','ms_access','man_acc_tally_erp','pagemaker_photoshop_gst_coreldraw', 'marks', 'course', 'image'
    )
    
    # Fields to show on the form view
    fields = (
        'name', 'space_id', 'certificate_id', 'father_name', 'mother_name', 
        'cs_fundamental_window', 'ms_word', 'ms_excel', 'ms_powerpoint', 'ms_outlook_internet','ms_access','man_acc_tally_erp','pagemaker_photoshop_gst_coreldraw', 'marks', 'course', 'image'
    )
    
    # Make `marks` read-only since it's calculated automatically
    readonly_fields = ('marks','certificate_id')
    
    # Enable search by name, father name, or certificate ID
    search_fields = ('name', 'father_name', 'certificate_id')
    
    # Add filter by course
    list_filter = ('course',)

# Register the model and the custom ModelAdmin class
admin.site.register(CandidateCertificate, CandidateCertificateAdmin)
