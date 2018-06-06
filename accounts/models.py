from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250, unique=True)
#
#     class Meta:
#         ordering = ('name', )
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'
#
#     def __str__(self):
#         return self.name

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=140, default='')
    city = models.CharField(max_length=50, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
