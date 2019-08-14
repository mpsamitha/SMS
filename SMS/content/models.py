from django.db import models
 
class Subject(models.Model):  
    subject_id = models.CharField(max_length=20, unique=True, error_messages={'unique':"This Subject ID has already been registered."})  
    subject_name = models.CharField(max_length=100)  
    subject_note = models.CharField(max_length=250)  
    
    class Meta:  
        db_table = "subject"

    def __str__(self):
    	return self.subject_name  