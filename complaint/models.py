from django.db import models
from HeyM8.settings import AUTH_USER_MODEL
from django.utils.timezone import now
from .choices import THEMES_TO_COMPLAIN_ON_NOTE


class NewsComplaint(models.Model):#represents complaint sent by user towards news

    class Meta:
        verbose_name = 'NewsComplaint'
        verbose_name_plural = 'NewsComplaints'

    complainant = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_complaints_news",
    )#user who has sent complaint

    date = models.DateField(

    )#when user has sent the complaint

    theme = models.CharField(
        max_length=15,
        choices=THEMES_TO_COMPLAIN_ON_NOTE
    )#reason why complaint was sent

    complaintSet = models.ForeignKey(
        "NewsComplaintSet",
        on_delete=models.CASCADE,
        related_name="complaints"
    )#complaintSet of news towards which complaint was sent


class ThoughtComplaint(models.Model):#represents complaint sent by user towards thought

    class Meta:
        verbose_name = 'ThoughtComplaint'
        verbose_name_plural = 'ThoughtComplaints'

    complainant = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_complaints_thought",
    )#user who has sent complaint

    date = models.DateField(

    )#when user has sent the complaint

    theme = models.CharField(
        max_length=15,
        choices=THEMES_TO_COMPLAIN_ON_NOTE
    )#reason why complaint was sent

    complaintSet = models.ForeignKey(
        "ThoughtComplaintSet",
        on_delete=models.CASCADE,
        related_name="complaints"
    )#complaintSet of thought towards which complaint was sent


class NewsComplaintSet(models.Model):#complaints obtained by news
    
    class Meta:
        verbose_name = 'newsComplaintSet'
        verbose_name_plural = 'newsComplaintSets'

    news = models.OneToOneField(
        "communities.News",
        on_delete=models.CASCADE,
        related_name="complaint_set"
    )#which news all these complaints belong to

    #how many complaints on different topics news this set belongs to has received
    nOfExtDugsPropComplaints = models.IntegerField()
    nOfSuicCallComplaints = models.IntegerField()
    nOfDiscreditComplaints = models.IntegerField()
    nOfAdultContentComplaints = models.IntegerField()


class ThoughtComplaintSet(models.Model):#complaints obtained by thought

    class Meta:
        verbose_name = 'thoughtComplaintSet'
        verbose_name_plural = 'thoughtComplaintSets'

    thought = models.ForeignKey(
        "users.Thought",
        on_delete=models.CASCADE,
        related_name="complaint_set"
    )#which thought all these complaints belong to

    #how many complaints on different topics thought this set belongs to has received
    nOfExtDrugsPropComplaints = models.IntegerField()
    nOfSuicCallComplaints = models.IntegerField()
    nOfDiscreditComplaints = models.IntegerField()
    nOfAdultContentComplaints = models.IntegerField()
