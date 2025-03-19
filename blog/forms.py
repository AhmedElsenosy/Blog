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

    def __init__(self, *args, **kwargs):
        super(Create_blog , self).__init__(*args, **kwargs)
        for field_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'