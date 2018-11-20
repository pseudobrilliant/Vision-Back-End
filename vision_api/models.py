from django.db import models

# Create your models here.
from django.db import models

class VisionUser(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=255, blank=True, default='')
    descriptor = models.CharField(max_length=4096, blank=True, default='')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.user

    def is_valid(self):

        return self.descriptor != "undefined" and self.created != "undefined"

