from django.db import models

from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

	STUDENT = 'student'
	TEACHER = 'teacher'

	USER_TYPE_CHOICES = [
		(STUDENT, 'student'),
		(TEACHER, 'teacher'),
	]

	user = models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
	phone_number = models.IntegerField(default=0,blank=True, null=True)
	user_address = models.CharField(max_length=150,blank=True, null=True)
	birth_date = models.DateField(blank=True, null=True)
	parent_name = models.CharField(max_length=150,blank=True, null=True)
	user_type = models.CharField(
        max_length=15,
        choices=USER_TYPE_CHOICES,
        default=STUDENT,
    ) 
	
	def __str__(self):
	  return self.user.username