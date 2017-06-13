from django.db import models
from concurrency.fields import TriggerVersionField

class MetadataMixin(models.Model):
	class Meta:
		abstract = True
	version = TriggerVersionField()

class Spam(MetadataMixin, models.Model):
	field = models.CharField(max_length=10, default="spam")

class Eggs(MetadataMixin, models.Model):
	field = models.CharField(max_length=10, default="eggs")
