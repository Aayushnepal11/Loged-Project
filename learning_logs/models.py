from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """ Creating the Topic Field for the users. """
    topic = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """ Returns the topic with it's name instead of an object. """
        return self.topic


class Entry(models.Model):
    """ Creating the Entries for the specific topic to be logged. """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        length = len(self.text)
        if length > 50:
            show_text =  f"{self.text[:50]}..."
        else:
            show_text = f"{self.text}"
        return show_text
