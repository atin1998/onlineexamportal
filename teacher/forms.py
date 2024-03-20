from django import forms
from django.contrib.auth.models import User
from . import models

# CHOICES = (
#         ("MALE","MALE"),
#         ("FEMALE","FEMALE"),
#         ("OTHER","OTHER"),
#     )

class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model=models.Teacher
        fields=['address','contact_no','profile_pic','gender']
        widgets = {
        # 'gender': forms.ChoiceField(choices=CHOICES),
        # 'date_of_birth':forms.DateInput(format='%d/%m/%Y')
        }