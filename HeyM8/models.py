#this file contains only abstract models which then base other models
from django.db import models
from django.utils.timezone import now
from HeyM8.settings import AUTH_USER_MODEL


class Note(models.Model):#base class for News and Thought

    class Meta:
        abstract=True

    isDeleted = models.BooleanField(

    )#indicates whether note was deleted because of receiving lot of complaints

    time = models.DateTimeField(

    )#when note was published

    isTemporary = models.BooleanField(

    )#if note expires in some time

    expiresOn = models.DateTimeField(

    )#if note is temporary - when it expires 

    content = models.CharField(
        max_length=900
    )#note itself

    def save(self, *args, **kwargs):
        self.time = now()
        return super(Note, self).save(*args, **kwargs)


class BreakingHistory(models.Model):

    class Meta:
        abstract=True

    #how many user's|communitie's notes have broken the rules
    nOfExtDugsPropBreakings = models.IntegerField(default=0)
    nOfSuicCallBreakings = models.IntegerField(default=0)
    nOfDiscreditBreakings = models.IntegerField(default=0)
    nOfAdultContentBreakings = models.IntegerField(default=0)


class Picture(models.Model):#base class of picture stored by

    class Meta:
        abstract=True

    picture = models.ImageField(
        null=True,
        blank=True,
    )#picture itself


