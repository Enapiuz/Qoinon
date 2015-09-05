from django.contrib import admin
from front.models import FaqItem
from django_summernote.admin import SummernoteModelAdmin

class FaqItemAdmin(SummernoteModelAdmin):
    model = FaqItem
    extra = 1

admin.site.register(FaqItem, FaqItemAdmin)