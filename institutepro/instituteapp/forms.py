from django import forms
from multiselectfield import MultiSelectFormField


class FeedBackFrom(forms.Form):
    name = forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter your Rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter your Feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Feedback'
            }
        )
    )


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )
    email = forms.EmailField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter your Mobile",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Mobile'
            }
        )
    )
    COURSES_CHOICES = (
        ('py', 'Python'),
        ('dj', 'Django'),
        ('ui', 'UI'),
        ('rest', 'REST API')
    )
    courses = MultiSelectFormField(max_length=200, choices=COURSES_CHOICES
                                   )
    SHIFT_CHOICES = (
        ('mng', 'Morning'),
        ('aftn', 'AfterNoon'),
        ('Eve', 'Evening'),
        ('night', 'Night')
    )
    shifts = MultiSelectFormField(max_length=200, choices=SHIFT_CHOICES)

    LOCATION_CHOICES = (
        ('hyd', 'Hyderabad'),
        ('bang', 'Banglore'),
        ('mum', 'Mumbai'),
        ('che', 'Chennai')
    )
    location = MultiSelectFormField(max_length=200, choices=LOCATION_CHOICES)

    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    gender = forms.CharField(
        widget=forms.RadioSelect(choices=GENDER_CHOICES)
    )

    start_date = forms.DateField(
        widget=forms.SelectDateWidget()
    )
