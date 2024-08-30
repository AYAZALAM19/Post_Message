from django.contrib import admin
from .models import ChaiVarity, ChaiCertificate, ChaiReview, Store

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)  # Corrected field name



class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')  # Removed extra space in 'chai '

# Register models with the correct admin classes
admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
