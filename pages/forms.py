from django import forms
from.models import Contact

class MyForm(forms.ModelForm):
    class meta:
        model = Contact
        field =['Full_Name', 'Email', 'Subject']
        label = {'Full_Name': "Name", 'Email':"Email", 'Subject':"Subject"}
