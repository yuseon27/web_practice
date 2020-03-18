from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Pictures(models.Model) : #{
    text = models.TextField()
    image = models.ImageField(upload_to="blogimg")
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(60, 120)])
#}

'''
ImageSpecField
- extension : format='JPEG'
- comp.quality : options={'quality':60}
'''