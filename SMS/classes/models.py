from django.db import models

from django.contrib.auth.models import User

class Classes(models.Model):

	A = 'A'
	B = 'B'
	C = 'C'

	CLASS_TYPE_CHOICES = [
		(A,'A'),
		(B,'B'),
		(C,'C'),
	]

	class_no = models.CharField(
		max_length=20,
		choices=CLASS_TYPE_CHOICES,
        default=A,
	)

	GRADE1 = 'GRADE 1'
	GRADE2 = 'GRADE 2'
	GRADE3 = 'GRADE 3'
	GRADE4 = 'GRADE 4'
	GRADE5 = 'GRADE 5'
	GRADE6 = 'GRADE 6'
	GRADE7 = 'GRADE 7'
	GRADE8 = 'GRADE 8'
	GRADE9 = 'GRADE 9'
	GRADE10 = 'GRADE 10'
	GRADE11 = 'GRADE 11'

	GRADE_TYPE_CHOICES = [
		(GRADE1,'GRADE 1'),
		(GRADE2,'GRADE 2'),
		(GRADE3,'GRADE 3'),
		(GRADE4,'GRADE 4'),
		(GRADE5,'GRADE 5'),
		(GRADE6,'GRADE 6'),
		(GRADE7,'GRADE 7'),
		(GRADE8,'GRADE 8'),
		(GRADE9,'GRADE 9'),
		(GRADE10,'GRADE 10'),
		(GRADE11,'GRADE 11'),
	]

	class_grade = models.CharField(
		max_length=20,
		choices=GRADE_TYPE_CHOICES,
		default=GRADE10,
	)

	# teacher = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='teacher')
	# student = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='student')

	class Meta:
		unique_together = ('class_no', 'class_grade',)
		db_table = "classes"

	def __unicode__(self):
		return u'%s' % self.class_grade

####################
class Classdetails(models.Model):
	classes = models.ForeignKey(Classes,on_delete=models.CASCADE)
	teacher = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='teacher')
	student = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='student')

	# class Meta:
	# 	db_table = "classdetails"
	def __str__(self):
		return self.classes.class_grade