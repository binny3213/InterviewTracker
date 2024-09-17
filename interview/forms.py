from django import forms
from .models import Interview
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class InterviewForm(forms.ModelForm):
    code_skills = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        label='Code Skills (0-10)'
    )
    project_presentation = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        label='Project Presentation (0-10)'
    )
    knowledge = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        label='Knowledge (0-10)'
    )
    confidence = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        label='Confidence (0-10)'
    )
    
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Interview Date'
    )
    
    class Meta:
        model = Interview
        fields = ['company_name', 'position',
                  'date', 'code_skills', 'project_presentation',
                  'knowledge', 'confidence', 'notes']
        
        