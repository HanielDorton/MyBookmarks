from datetime import datetime
from django.db import models

class Categories(models.Model):
    name = models.CharField(blank=False, max_length=100)
    def __unicode__(self):
        return self.name
	
	class Meta:
		ordering = ['name']

class Link(models.Model):
	title = models.CharField(max_length=100, blank=False)
	url = models.URLField()
	created_on = models.DateTimeField(default=datetime.now())
	last_accessed = models.DateTimeField(default=datetime.now())
	views = models.IntegerField(default=0)
	channels = models.ManyToManyField(Categories)
	current = models.BooleanField(default=False)
	notes = models.TextField()
	def __unicode__(self):
		return self.title
