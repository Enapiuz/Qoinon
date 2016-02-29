from django.contrib import admin
from .models import FaqItem, FaqCategory, ContactForm
from django_summernote.admin import SummernoteModelAdmin


class FaqItemAdmin(SummernoteModelAdmin):
    model = FaqItem
    extra = 1


class FaqCategoryAdmin(SummernoteModelAdmin):
    get_model_perms = lambda self, request: {}


class ContactFormAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'text')
    model = ContactForm
    extra = 1


admin.site.register(FaqItem, FaqItemAdmin)
admin.site.register(FaqCategory, FaqCategoryAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
