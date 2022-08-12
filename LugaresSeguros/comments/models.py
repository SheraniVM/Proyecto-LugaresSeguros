from django.db import models
from places.models import Place

# Create your models here.

class Comment(models.Model):

    place = models.ForeignKey(Place, on_delete=models.CASCADE) #FK with place, if Place deleted comment must be too
    comment = models.TextField() ##Equivalent to a Text area
    created = models.DateTimeField(auto_now_add=True) #This date won't be modified anytime

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.comment

