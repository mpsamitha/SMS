from django import forms

from attendance.models import Attendance

class AttendanceForm(forms.ModelForm):  
    class Meta:  
        model = Attendance  
        fields = "__all__"