from django.contrib import admin
from .models import about_us, sociallinks, company_address, copyright, dynAddress
# Register your models here.


admin.site.register(about_us)
admin.site.register(sociallinks)
admin.site.register(company_address)
admin.site.register(copyright)
admin.site.register(dynAddress)