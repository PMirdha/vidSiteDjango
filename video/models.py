from django.db import models

# Create your models here.

class Playlist(models.Model):

	title = models.CharField(max_length=100)
	discription = models.CharField(max_length=100)
	thumbnail = models.CharField(max_length=100)

	def __str__(self):
		return str(self.pk)+". "+self.title



class Score(models.Model):

	playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	summary = models.CharField(max_length=100)
	url_link = models.CharField(max_length=100)

	def __str__(self):
		return self.title+"-"+self.summary