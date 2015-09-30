from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
	return (self.question_text)

    def was_published_recently(self):
	return (self.pub.date >= timezone.now())

datetime.timedelta(days=1)

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

<<<<<<< HEAD
    def __str__(self):
	return (self.choice_text)
=======
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
>>>>>>> 02ee4c004d3d3a2a09b976f2f6af290b1d9ec136
