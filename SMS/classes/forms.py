from django import forms

from classes.models import Classes, Classdetails

class ClassesForm(forms.ModelForm):
  
    class Meta:  
        model = Classes  
        fields = "__all__"

class ClassdetailsForm(forms.ModelForm):
  
    class Meta:  
        model = Classdetails  
        fields = "__all__"