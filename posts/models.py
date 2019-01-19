from django.conf import settings
from django.urls import reverse
from django.db import models
from .validators import validate_content
# Create your models here.

class Posts(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	content = models.CharField(max_length=200, validators = [validate_content])
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	#last_name = models.CharField()
	
	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"pk":self.pk})

	# def clean(self, *args, **kwargs):
	# 	content = self.content
	# 	if content == 'abc':
	# 		raise ValidationError("cannot  containt ABC")
	# 	return super(Posts, self).clean(*args, **kwargs)

