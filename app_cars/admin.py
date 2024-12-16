from django.contrib import admin
from .models import Car, Test
from django.utils.html import format_html
from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from multiselectfield import MultiSelectField
# Register your models here.


class CarAdminForm(forms.ModelForm):
    # description = RichTextField()  # Define the RichTextField in your form
    description = forms.CharField(widget=CKEditorWidget())
    # features = MultiSelectField(default=[])

    class Meta:
        model = Car
        fields = '__all__'


# @admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    form = CarAdminForm

    def thumbnail(self, object):
        return format_html("<img src='{}' style='width:40px; border-radius:20%;'> ".format(object.car_photo.url))

    thumbnail.short_description = 'Car Photo'
    list_display = ('id', 'thumbnail', 'car_title', 'state', 'city', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title',)
    list_editable = ('is_featured',)
    search_fields = ('car_title','state', 'city', 'is_featured')
    list_filter = ('body_style', 'city', 'is_featured')
    # list_per_page = 4


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'choices')


admin.site.register(Car, CarAdmin)
admin.site.register(Test, TestAdmin)