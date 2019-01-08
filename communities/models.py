from django.db import models
from django.utils.translation import gettext_lazy as _
from HeyM8.settings import AUTH_USER_MODEL
from . import choices
from django.utils.timezone import now
from django.utils import timezone
from HeyM8.models import Note, BreakingHistory


class Community(models.Model):#organization ruled by one user spreading content for it's members

    class Meta:
        verbose_name = _('community')
        verbose_name_plural = _('communities')
    
    isBanned = models.BooleanField(
        default=False,
    )#indicates whether this community is banned

    bannedTill = models.DateField(
        null=True,
    )#if community is banned specifies the date when it is is unbanned

    name = models.CharField(
        max_length=20,
    )#name of the community

    finalRating = models.FloatField(

    )#number of community's rating based on assessments

    nOfMembers = models.IntegerField(

    )#number of members


class CommGovernance(models.Model):#people who teke part in managing community

    class Meta:
        verbose_name = "CommGovernance"
        verbose_name_plural = "CommGovernances"

    community = models.OneToOneField(
        "communities.Community",
        on_delete=models.CASCADE,
        related_name="governance"
    )#community which is managed by this governance

    mainAdmin = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ruled_communities_governances"
    )#user who has created community, can rule other admins and can pass his permissions to other admin

    admins = models.ManyToManyField(
        AUTH_USER_MODEL,
        related_name="managed_communities_governances"
    )#users who got admin status via mainAdmin's invitation

    feedback = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="feedback_Communities_Governances"
    )#user who is responsible for feedback



class CommunityInfo(models.Model):#info about community

    community = models.OneToOneField(
        "communities.Community",
        on_delete=models.CASCADE,
        related_name="community_Info"
    )

    class Meta:
        verbose_name = "CommunityInfo"
        verbose_name_plural = "CommunityInfos"

    status = models.CharField(
        max_length=35
    )

    contentType = models.CharField(
        max_length=5,
        choices=choices.COMMUNITY_CONTENT_TYPE,
    )

    description = models.CharField(
        max_length=100
    )


class News(Note):#core value unit created by Community
    
    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
    
    community = models.ForeignKey(
        Community,
        on_delete=models.CASCADE,
        related_name="news"
    )

    pictures = models.ManyToManyField(
        'communities.CommPicture',
        related_name="attached_To"
    )#pictures attached to the news


class CommAlbum(models.Model):

    name = models.CharField(
        max_length=35,
    )#album's name

    description = models.CharField(
        max_length=100
    )#album's description

    custom = models.BooleanField(
        default=True,
    )#all pictures and thought pictures can not be deleted

    community = models.ForeignKey(
        'communities.Community',
        on_delete=models.CASCADE,
        related_name='albums',
    )#community it belongs to

    mainPicture = models.ForeignKey(
        "communities.CommPicture",
        on_delete=models.SET_NULL,
        null=True,
        related_name='album_Main_For',
    )#picture which is "face" of the album


class CommPicture(models.Model):

    album = models.ForeignKey(
        "communities.CommAlbum",
        on_delete=models.CASCADE,
        related_name="pictures"
    )#album it belongs to

    uploadTime = models.DateTimeField(
        default=timezone.now,
    )#when picture was uploaded    

    picture = models.ImageField(

    )#picture itself


class CommAssessment(models.Model):#community assessment sent by user
    
    class Meta:
        verbose_name = "CommAssessment"
        verbose_name_plural = "CommAssessments"

    sender = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_Community_Assessments"
    )#user who sent assessment

    community = models.ForeignKey(
        "communities.Community",
        on_delete=models.CASCADE,
        related_name="received_Community_Assessments"
    )#rated community

    quality = models.IntegerField(
        default=0,
    )#quality assessment/ assessment criterion

class CommBreakingHistory(BreakingHistory):

    community = models.OneToOneField(
        "communities.Community",
        on_delete=models.CASCADE,
        related_name="breaking_History"
    )

    class Meta:
        verbose_name = 'CommunityBreakingHistory'
        verbose_name_plural = 'CommunityBreakingHistories'
