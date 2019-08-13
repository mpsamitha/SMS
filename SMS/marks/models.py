from django.db import models

from django.contrib.auth.models import User

from classes.models import Classes

from exam.models import Exam

from content.models import Subject

from decimal import Decimal

class Marks(models.Model):
	user_id = models.OneToOneField(User,on_delete=models.CASCADE)
	classes = models.ForeignKey(Classes,default=None,on_delete=models.CASCADE,related_name='classes')
	exam = models.ForeignKey(Exam,default=None,on_delete=models.CASCADE,related_name='exam')
	subject1 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject1',null=True)
	marks1 = models.DecimalField(max_digits=3, decimal_places=0, default=000)
	subject2 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject2',null=True)
	marks2 = models.DecimalField(max_digits=3, decimal_places=0, default=000)
	subject3 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject3',null=True)
	marks3 = models.DecimalField(max_digits=3, decimal_places=0, default=000)
	subject4 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject4',null=True)
	marks4 = models.DecimalField(max_digits=3, decimal_places=0, default=000)
	subject5 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject5',null=True)
	marks5 = models.DecimalField(max_digits=3, decimal_places=0, default=000)
	subject6 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject6',null=True)
	marks6 = models.DecimalField(max_digits=3, decimal_places=0, default=000)
	subject7 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject7',null=True)
	marks7 = models.DecimalField(max_digits=3, decimal_places=0, default=000)
	subject8 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject8',null=True)
	marks8 = models.DecimalField(max_digits=3, decimal_places=0, default=000)
	subject9 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject9',null=True)
	marks9 = models.DecimalField(max_digits=3, decimal_places=0, default=000)
	subject10 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject10',null=True)
	marks10 = models.DecimalField(max_digits=3, decimal_places=0, default=000)
	total = models.DecimalField(max_digits=3, decimal_places=0, default=000)
	# subject11 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject')
	# subject12 = models.ForeignKey(Subject,default=None,on_delete=models.CASCADE,related_name='subject')


	class Meta:
		db_table = "marks"
		
