from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length=500)

    def __self__(self):
        return self.title