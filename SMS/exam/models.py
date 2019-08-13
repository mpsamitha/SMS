from django.db import models

class Exam(models.Model):
	exam_id = models.CharField(max_length=255)
	exam_name = models.CharField(max_length=255)
	start_date = models.DateTimeField(default='0000-00-00 00:00:00')
	end_date = models.DateTimeField(default='0000-00-00 00:00:00')

	class Meta:
		db_table = "exam"