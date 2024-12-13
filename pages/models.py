from django.db import models

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    url_facebook = models.URLField(max_length=100)
    url_twitter = models.URLField(max_length=100)
    url_google_plus = models.URLField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}, {}".format(self.first_name, self.last_name)
