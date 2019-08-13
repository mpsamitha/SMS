from django import forms

from marks.models import Marks

class MarksForm(forms.ModelForm):  
    class Meta:  
        model = Marks  
        fields = "__all__"