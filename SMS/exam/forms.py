from django import forms

from exam.models import Exam

class ExamForm(forms.ModelForm):  
    class Meta:  
        model = Exam  
        fields = "__all__"