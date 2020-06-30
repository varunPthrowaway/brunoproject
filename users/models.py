from django.db import models
from django.contrib.auth.models import User
from PIL import Image

CATEGORY_CHOICES = [
            (0, 'Owner'),
            (1, 'Pet Lover'),
            (2, 'Animal Shelter')
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    location = models.CharField(max_length=256, default="")
    category = models.IntegerField(
        choices=CATEGORY_CHOICES,
        default=0
    )
    contact_no = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def category_verbose(self):
        return dict(CATEGORY_CHOICES)[self.category]
