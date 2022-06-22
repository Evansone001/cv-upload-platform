import email
from django import forms
from django.forms import ModelForm
from .models import Profile
from django_file_form.forms import FileFormMixin, UploadedFileField

# create a professional form


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'second_name', 'last_name', 'gender', 'id_no',
                  'phone_number', 'email', 'ward', 'constituences', 'education_level', 'graduation_year', 'resume'
                  ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'id_no': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'ward': forms.Select(attrs={'class': 'form-control'}),
            'constituences': forms.Select(attrs={'class': 'form-control'}),
            'education_level': forms.Select(attrs={'class': 'form-control'}),
            'graduation_year': forms.TextInput(attrs={'class': 'form-control'}),

        }
# class Meta:
  #      model= Skill
  #      fields =['skill ']
