from django.forms import ModelForm
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UploadSkill, SkillRequest, Feedback



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']




class SkillForm(forms.ModelForm):
    class Meta:
        model = UploadSkill
        fields = ['name', 'description', 'category', 'file']




class SkillRequestForm(forms.ModelForm):
    class Meta:
        model = SkillRequest
        fields = ['skill_name', 'skill_description']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_text']








