from django.db import models
from django.contrib.auth.models import User
from .constants import *



class AppUser(User):
	pass

	def __repr__(self):
		return f'user.username'


# Create your models here.
class Profession(models.Model):
	job_title = models.CharField(max_length=100)
	company = models.CharField(max_length=200)

	def __repr__(self):
		return f'{self.id} - {self.job_title} - {self.company}'


class Education(models.Model):
	degree = models.CharField(max_length=100)
	university = models.CharField(max_length=200)

	def __repr__(self):
		return f'{self.id} - {self.degree} - {self.university}'



def user_images(instance, filename):
	return f'user_images/user_{instance.user.id}/{filename}'

class ProfileImages(models.Model):
	image1 = models.ImageField(upload_to=user_images, height_field='image1_height', width_field='image1_width', max_length=100)
	image2 = models.ImageField(upload_to=user_images, height_field='image2_height', width_field='image2_width', max_length=100)
	image3 = models.ImageField(upload_to=user_images, height_field='image3_height', width_field='image3_width', max_length=100)
	image4 = models.ImageField(upload_to=user_images, height_field='image4_height', width_field='image4_width', max_length=100)
	image5 = models.ImageField(upload_to=user_images, height_field='image5_height', width_field='image5_width', max_length=100)
	image6 = models.ImageField(upload_to=user_images, height_field='image6_height', width_field='image6_width', max_length=100)

	def __repr__(self):
		return f'{self.id}'


class PersonalInformation(models.Model):
	f_name 		= models.CharField(max_length=50, null=False, blank=False)
	l_name 		= models.CharField(max_length=50, null=False, blank=False)
	location 	= models.CharField(max_length=200, null=False, blank=False)
	education 	= models.CharField(max_length=200)
	instagram 	= models.CharField(max_length=100)
	email 		= models.EmailField()
	date_of_birth = models.DateField(auto_now=False, null=False, blank=False)	
	bio 		= models.TextField(max_length=500)
	age 		= models.IntegerField()
	mobile_number = models.PositiveBigIntegerField()
	mobile_number_verified = models.BooleanField(default=False)
	photo_verified 	=  models.BooleanField(default=False)
	work 		= models.ForeignKey('Profession', on_delete=models.CASCADE)
	images 		= models.ForeignKey('ProfileImages', on_delete=models.CASCADE)
	
	height 		= models.FloatField()	
	sexuality 	= models.CharField(max_length=1, choices=Sexuality.choices, default=Sexuality.MALE)
	purpose 	= models.CharField(max_length=1, choices=Purpose.choices, default=Purpose.CHAT)
	activity_interests = models.CharField(max_length=1, choices=Activity.choices, default=Activity.RUNNING)
	profile_interest = models.CharField(max_length=2, choices=ProfileInterest.choices, default=ProfileInterest.MALE_AND_FEMALE_BOTH)
	children 	= models.CharField(max_length=3, choices=ChildrenInterest.choices, default=ChildrenInterest.DONT_WANNA_TELL)
	drinking 	= models.CharField(max_length=3, choices=DrinkingInterest.choices, default=DrinkingInterest.NEVER)
	smoking 	= models.CharField(max_length=3, choices=SmokingInterest.choices, default=SmokingInterest.NEVER)
	languages 	= models.CharField(max_length=20, choices=Languages.choices, default=Languages.HINDI)
	relationship_status = models.CharField(max_length=1, choices=RelationshipStatus.choices, default=RelationshipStatus.SINGLE)
	start_sign 	= models.CharField(max_length=3, choices=StarSign.choices, default=StarSign.LIBRA)
	pets 		= models.CharField(max_length=1, choices=PetsInterest.choices, default=PetsInterest.NO)
	religion 	= models.CharField(max_length=20, choices=Religion.choices, default=Religion.NOT_STARTED)
	personality = models.CharField(max_length=1, choices=Personality.choices, default=Personality.INTROVERT)
	
	def __repr__(self):
		return f'{self.personal_information.f_name}{self.personal_information.l_name}'



class Profile(models.Model):
	user = models.ForeignKey('AppUser', on_delete=models.CASCADE)
	personal_information = models.ForeignKey('PersonalInformation', on_delete=models.CASCADE)	
	coins = models.PositiveIntegerField(default=250)
	likes_given = models.ManyToManyField('Profile', related_name='given')
	likes_recieved = models.ManyToManyField('Profile', related_name='recieved')
	visibility_area = models.PositiveIntegerField()
	active = models.BooleanField(default=True)

	def __repr__(self):
		return f'{self.user.username} - {self.personal_information.f_name} {self.personal_information.l_name}'

