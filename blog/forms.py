from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Feedback form"""
    # captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control border"}),
        #     "email": forms.EmailInput(attrs={"class": "form-control border"}),
        #     "text": forms.Textarea(attrs={"class": "form-control border"})
        # }
