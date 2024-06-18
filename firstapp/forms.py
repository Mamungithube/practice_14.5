from django import forms 
from django.forms.widgets import NumberInput
import datetime
from .models import MyModel

class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)) 
    value = forms.DecimalField()
    message = forms.CharField(max_length=10)
    email_address = forms.CharField(label= 'Enter your email address')
    first_name = forms.CharField(initial= 'your name')
    agree_k = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)

    FAVORITE_COLORS_CHOICES = [
            ('blue', 'Blue'),
            ('green', 'Green'),
            ('black', 'Black'),
            ]   
    color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES) 
    
    # Radio select

    
    FAVORITE_COLORS_CHOICES = [
            ('blue', 'Blue'),
            ('green', 'Green'),
            ('black', 'Black'),
            ]   
    fav_color = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS_CHOICES) 


    FAVORITE_COLORS_CHOICES = [
            ('blue', 'Blue'),
            ('green', 'Green'),
            ('black', 'Black'),
            ]   
    multi_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES) 
    
    FAVORITE_COLORS_CHOICES = [
            ('blue', 'Blue'),
            ('green', 'Green'),
            ('black', 'Black'),
            ]   
    colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES) 

    title = forms.CharField()
    description = forms.CharField()
    roll = forms.IntegerField(help_text='Enter 6 digit roll number')
    password = forms.CharField(widget=forms.PasswordInput)



class MymodelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'