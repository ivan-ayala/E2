from django.db import models

class Zombie(models.Model):
	name = models.CharField(max_length=50)
	cemetery = models.CharField(max_length=25)

	def __unicode__(self):
		return '%s.- %s' % (self.id, self.name,)

	class Meta:
		ordering = ['-name']

class Tweet(models.Model):
	status = models.CharField(max_length=140)
	zombie = models.ForeignKey('Zombie', related_name='tweets')
	created_at = models.DateTimeField(auto_now_add=True)	