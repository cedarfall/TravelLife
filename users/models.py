from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
	website = models.CharField(max_length=150, default='', blank=True)
	twitter = models.CharField(max_length=150, default='', blank=True)
	linkedin = models.CharField(max_length=150, default='', blank=True)
	facebook = models.CharField(max_length=150, default='', blank=True)


	def __str__(self):
		return f'{self.user.username} Profile'
	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		output_size = (800, 800)
		img.thumbnail(output_size)
		img.save(self.image.path)