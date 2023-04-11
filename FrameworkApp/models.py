from django.db import models
from django.contrib.auth.models import User
from .constants import *


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



class ProfileImages(models.Model):
	image_one = models.ImageField()
	image_two = models.ImageField()
	image_three = models.ImageField()
	image_four = models.ImageField()
	image_five = models.ImageField()
	image_six = models.ImageField()

	def __repr__(self):
		return f'{self.id}'



class PersonalInformation(models.Model):
	f_name = models.CharField(max_length=50, null=False, blank=False)
	l_name = models.CharField(max_length=50, null=False, blank=False)
	email = models.EmailField()
	age = models.PositiveIntegerField(max=150, min=18)
	date_of_birth = models.DateField(null=False, blank=False)
	location = models.CharField(max_length=200, null=False, blank=False)
	work = models.ForeignKey('Profession')
	bio = models.CharField(max_length=500)
	verified =  models.BooleanField(default=False)
	education = models.CharField(max_length=200)
	instagram = models.CharField(max_length=100)
	mobile_number = models.PositiveIntegerField(min=6000000000, max=9999999999)
	mobile_number_verified = models.BooleanField(default=False)
	sexuality = models.CharField(max_length=1, choices=Sexuality.choices, default=Sexuality.MALE)
	purpose = models.CharField(max_length=1, choices=Purpose.choices, default=Purpose.CHAT)
	activity_interests = models.ChoiceField(max_length=1, choices=Activity.choices, default=Activity.RUNNING)
	profile_interest = models.CharField(max_length=2, choices=ProfileInterest.choices, default=ProfileInterest.MALE_AND_FEMALE_BOTH)
	images = models.ForeignKey('ProfileImages')
	height = models.PositiveIntegerField()
	children = models.ChoiceField(max_length=3, choices=ChildrenInterest.choices, default=ChildrenInterest.DONT_WANNA_TELL)
	drinking = models.ChoiceField(max_length=3, choices=DrinkingInterest.choices, default=DrinkingInterest.NEVER)
	smoking = models.ChoiceField(max_length=3, choices=SmokingInterest.choices, default=SmokingInterest.NEVER)
	languages = models.ChoiceField(max_length=20, choices=Languages.choices, default=Languages.HINDI)
	relationship_status = models.ChoiceField(max_length=1, choices=RelationshipStatus.choices, default=RelationshipStatus.SINGLE)
	start_sign = models.ChoiceField(max_length=3, choices=StarSign.choices, default=StarSign.Libra)
	pets = models.ChoiceField([])
	religion = models.ChoiceField([])
	personality = models.ChoiceField([])
	
	def __repr__(self):
		return f'{self.personal_information.f_name}{self.personal_information.l_name}'



class Profile(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	personal_information = models.ForeignKey('PersonalInformation', on_delete=models.CASCADE)	
	coins = models.PositiveIntegerField(min=0, default=250)
	likes_given = models.ManyToManyField('Profile')
	likes_recieved = models.ManyToManyField('Profile')
	visibility_area = models.PositiveIntegerField(min=0, max=40000)
	active = models.BooleanField(default=True)

	def __repr__(self):
		return f'{self.user.username} - {self.personal_information.f_name}{self.personal_information.l_name}'

