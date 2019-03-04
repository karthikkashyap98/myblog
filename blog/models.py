 from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	timestamp = models.DateTimeField(auto_now_add = True)
	cover = models.ImageField(upload_to = "all_covers/", default="all_covers/cover.png")

	def __str__(self):
		return f"{self.id}.{self.title}"


   