from django.db import models
from django.utils.translation import gettext_lazy as __RT__


class Sexuality(models.TextChoices):
	MALE = "M", __RT__("Male")
	FEMALE = "F", __RT__("Female")
	TRANSGENDER = "T", __RT__("Transgender")


class Purpose(models.TextChoices):
	CHAT = "C", __RT__("Chat")
	FRIENDSHIP = "F", __RT__("Friendship")
	DATE = "D", __RT__("Date")
	RELATIONSHIP = "R", __RT__("Relationship")



class Activity(models.TextChoices):
	RUNNING = "R", __RT__("Running")
	CYCLING = "C", __RT__("Cycling")
	DANCING = "D", __RT__("Dancing")
	SINGING = "S", __RT__("Singing")


class ProfileInterest(models.TextChoices):
	MALE = "M", __RT__("Male")
	FEMALE = "F", __RT__("Female")
	TRANSGENDER = "T", __RT__("Transgender")
	MALE_AND_FEMALE_BOTH = "MF", __RT__("Male and Female Both")


class ChildrenInterest(models.TextChoices):
	DONT_WANNA_TELL = "DWT", __RT__("Don't wanna tell")



class DrinkingInterest(models.TextChoices):
	NEVER = "NVR", __RT__("Never had never will")
	OCCATIONALLY ="OCC", __RT__("Occationally")

class SmokingInterest(models.TextChoices):
	NEVER = "NVR", __RT__("Never had never will")
	OCCATIONALLY ="OCC", __RT__("Occationally")


class Languages(models.TextChoices):
	HINDI = "HINDI", __RT__("Hindi")
	ENGLISH ="ENGLISH", __RT__("English")	

class RelationshipStatus(models.TextChoices):
	SINGLE = "S", __RT__("Single")
	ENGAGED ="E", __RT__("Engaged")
	MARRIED = "M", __RT__("Married")
	DIVORCED = "D", __RT__("Devorced")

class StarSign(models.TextChoices):
	LIBRA = "LIB", __RT__("Libra")

class PetsInterest(models.TextChoices):
	NO = "N", __RT__("Not interested")
	DOG = "D", __RT__("Dog lover")
	CAT = "C", __RT__("Cat lover")


class Religion(models.TextChoices):
	NOT_STARTED = "NOT_STARTED", __RT__("Not started")
	HINDU = "HINDU", __RT__("Hindu")
	MUSLIM = "MUSLIM", __RT__("Muslim")
	OTHER = "OTHER", __RT__("Other")

class Personality(models.TextChoices):
	INTROVERT = "I", __RT__("Introvert")
	EXTROVERT = "E", __RT__("Extrovert")
	AMBIVERT = "A", __RT__("Ambivert")
