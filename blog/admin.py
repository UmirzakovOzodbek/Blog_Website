from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post, Reviews


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы к фильму"""
    list_display = ("name", "post", "email", "parent", "id")
    readonly_fields = ("name", "email")
