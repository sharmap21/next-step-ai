from django import forms

class CareerForm(forms.Form):
    EDUCATION_LEVELS = [
        ('High School', 'High School'),
        ('Bachelor\'s', 'Bachelor\'s'),
        ('Master\'s', 'Master\'s'),
        ('PhD', 'PhD')
    ]

    skills = forms.CharField(
        widget=forms.HiddenInput(),
        required=True,
        error_messages={'required': 'Please enter at least one skill.'}  # Custom error message
    )
    
    education = forms.ChoiceField(
        choices=[('', '-- Select Education --'),  # Initially blank
                 ('High School', 'High School'),
                 ('Bachelor\'s', 'Bachelor\'s'),
                 ('Master\'s', 'Master\'s'),
                 ('PhD', 'PhD')],
        required=True,
        error_messages={'required': 'Please select your education level.'}
    )

    field_of_study = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'e.g., Computer Science, Business'}),
        error_messages={'required': 'Please enter your field of study.'}
    )
