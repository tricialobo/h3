from django.db import models


class Animal(models.Model):
	CAT = ("cat", "Cat")
	DOG = ("dog", "Dog")

	name = models.CharField(max_length=60)
	alias = models.CharField(max_length=60)
	type = models.CharField(choices=[CAT, DOG], help_text="Type of animal", max_length=10)

# class Human(models.Model)
# 	name = models.CharField(max_length=60)

def __str__(self):
	return self.name
