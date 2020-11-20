from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

PLATFORM_CHOICES = [
    ('Steam', u'Steam'),
    ('Epic Games Store', u'Epic Games Store'),
    ('Origin', u'Origin'),
    ('Battle.net', u'Battle.net'),
    ('Riot Client', u'Riot Client'),
    ('Not listed', u'Not listed')
]


class Member(AbstractUser):
    handle = models.CharField(max_length=32)
    is_pro = models.BooleanField(default=False)

    twitter = models.CharField(max_length=32, blank=True, null=True)
    instagram = models.CharField(max_length=32, blank=True, null=True)
    twitch = models.CharField(max_length=32, blank=True, null=True)
    youtube = models.CharField(max_length=64, blank=True, null=True)



    ip_address = models.CharField(max_length=20, blank=True, null=True)
    ip_information = models.TextField(max_length=500, null=True, blank=True)



    def __str__(self):
        return f'{self.username}'


class Game(models.Model):
    title = models.CharField(max_length=64)
    developer = models.CharField(max_length=64)
    platform = models.CharField(max_length=32, choices=PLATFORM_CHOICES)
    release_date = models.DateField(auto_now=True)
    players = models.ManyToManyField(Member)
    
    def __str__(self):
        return f'{self.title} from {self.developer} ({self.platform})'