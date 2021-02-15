from django.db import models
# Defining database 
class Post(models.Model):
    name  = models.CharField(max_length=250)
    caption = models.CharField(max_length=250)
    url = models.URLField()
    objects = models.Manager()
    # Adding unique constraint to make sure duplicate data doesn't get added
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name','caption','url'], name='UniqueConstraint')
        ]

    def __str__(self):
        return self.name