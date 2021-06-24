from django import forms

class FileForm(forms.Form):    
    test_x = forms.FileField()
