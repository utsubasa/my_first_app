from django import forms

class FileForm(forms.Form):    
    #train_x = forms.FileField() 
    #train_y = forms.FileField() 
    test_x = forms.FileField() 