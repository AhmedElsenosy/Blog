from django import forms
from .models import *

class Edit_blog (forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('author',)

    def __init__(self, *args, **kwargs):
        super(Edit_blog , self).__init__(*args, **kwargs)
        for field_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class Create_blog (forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('author',)
        widgets = {
            'tags': forms.TextInput(attrs={'data-role': 'tagsinput'}), 
        }

    def __init__(self, *args, **kwargs):
        super(Create_blog, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        # Add placeholder for tags field
        self.fields['tags'].widget.attrs['placeholder'] = 'Add tags separated by commas'


class Contact_us_form (forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(Contact_us_form , self).__init__(*args, **kwargs)
        for field_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'