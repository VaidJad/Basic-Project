from django import forms 
from django.core import validators

def start_with_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('FIRST LETTER MUST BE Z')

class FormName(forms.Form):
    name=forms.CharField(validators=[start_with_z])
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    bot_catch=forms.CharField(required=False, 
                              widget=forms.HiddenInput,
                              validators=[validators.MaxLengthValidator(0)]
                                )
    verify_mail=forms.CharField(label="Enter email again")

    def clean(self):
        clean_data=super().clean()
        email=clean_data['email']
        vmail=clean_data['verify_mail']

        if email != vmail:
            raise forms.ValidationError("Email Not Matched")