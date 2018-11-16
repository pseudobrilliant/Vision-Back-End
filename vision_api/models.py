from django.db import models

# Create your models here.
from django.db import models

class VisionUser(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=255, blank=True, default='')
    left = models.CharField(max_length=255, blank=True, default='')
    right = models.CharField(max_length=255, blank=True, default='')
    center = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.user
