from django.db import models

from django.contrib.auth.models import User

class Attendance(models.Model):
	# classes = models.ForeignKey(Classes,default=None,on_delete=models.CASCADE,related_name='classes')
	# user_id = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='student')
	user_id = models.OneToOneField(User,on_delete=models.CASCADE)
	rfid_uid = models.CharField(max_length=255)
	punch_time = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(default='0000-00-00 00:00:00')

	class Meta:
		db_table = "attendance"
		
