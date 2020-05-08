from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class BNB(models.Model):
	name = models.CharField(max_length=100)
	rooms = models.CharField(max_length=1)
	price = models.CharField(max_length=10)
	start_date = models.DateTimeField(default=timezone.now)
	end_date = models.DateTimeField(default=timezone.now)
	amenities = models.CharField(max_length=100)
	image = models.ImageField(default='bnb_pics/default.jpg', upload_to='bnb_pics')
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def save(self, *args, **kwargs):

		super().save(*args, **kwargs)

		img = Image.open(self.image.path)
		output_size = (600, 600)
		img.thumbnail(output_size)
		img.save(self.image.path)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('bnb-detail', kwargs={'pk': self.pk})
