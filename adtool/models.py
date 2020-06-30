from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from PIL import Image
from django import forms

CRITERIA_CHOICES = (
        (0, 'Adoption'),
        (1, 'Caretaking'),
        (2, 'Fostering'),
    )

class ListedPet(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    criteria = models.IntegerField(
        choices=CRITERIA_CHOICES,
        default=0
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField('date published', default=timezone.now)
    start_date = models.DateTimeField('date activity start', default=timezone.now)
    end_date = models.DateTimeField('date activity end', default=timezone.now)
    description = models.TextField(default='')
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def criteria_verbose(self):
        return dict(CRITERIA_CHOICES)[self.criteria]


