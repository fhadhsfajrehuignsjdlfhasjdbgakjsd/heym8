import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
from HeyM8.settings import AUTH_USER_MODEL
from . import choices 
from HeyM8.models import Note, BreakingHistory
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractUser):#core User model
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract=False

    email = models.EmailField(
        _('email address'), 
        unique=True,
        error_messages={'unique': _("A user with that username already exists."),},
        )#unique field

    username = models.CharField(
        _('username'),
        max_length=30,
    )#override to reduce max_len and remove unique option

    uniqueURL = models.CharField(
        max_length=25,
        unique=True,
        blank=True,
        null=True,
    )#when accessing https://HeyM8.com/user/{{uniqueURL}} show user's page, 
    #first uniqueURL=id
    #can't be entirely numeric

    USERNAME_FIELD = 'email'#unique field

    REQUIRED_FIELDS = ['username']#required fields

    isDeleted = models.BooleanField(
        default=False,
    )#indicates whether this account is deleted/instaed of deleting account set this field to True

    isBanned = models.BooleanField(
        default=False,
    )#indicates whether this user is banned

    bannedTill = models.DateField(
        null=True,
    )#if user is banned specifies the date when he is unbanned

    finalRating = models.FloatField(
        default=0.0,
    )#final user's rating based on his rating(RateMate)

    mateList = models.ManyToManyField(
        AUTH_USER_MODEL, 
        related_name="mates"
    )#users added by this user

    sentReqs = models.ManyToManyField(
        AUTH_USER_MODEL,
        related_name="received_Reqs"
    )#user to which this user has sent add request

    communitiesList = models.ManyToManyField(
        "communities.Community", 
        related_name="members"
    )#communities which user has entolled 

    lastSeen = models.DateTimeField(
        "was online for the last time",
        default=timezone.now,
    )#when user was online for the last time

    def __str__(self):
        return "Username: {}, email: {}".format(self.username, self.email)

    def get_short_name(self):#overrides AbstractUser's function because this model has no name and second_name
        return self.username


class StatisticInfo(models.Model):#user's statistics

    class Meta:
        verbose_name = 'statisticInfo'
        verbose_name_plural = 'statisticInfos'

    user = models.OneToOneField(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="statistic_Info"
    )

    confirmationKey = models.UUIDField(
        "key to redirect in email",
        null=True,
    )#key to redirect in email

    isActive = models.BooleanField(
        default=True,
    )#indicates whether user actively uses service (whether he can be found via MeetMate)

    nOfReceivedSpamComplaints = models.IntegerField(
        default=0,
    )#number of received spam complaints

    usedMeetMate = models.BooleanField(
        default=False,
    )#indicates if user has ever foud mate using MeetMate

    usedRateMate = models.BooleanField(
        default=False,
    )#indicates if user has ever foud mate using RateMate


class PersonalInfo(models.Model):#user's pesonal info

    class Meta:
        verbose_name = 'personalInfo'
        verbose_name_plural = 'personalInfos'

    user = models.OneToOneField(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="personal_Info",
    )#user this info belongs to

    status = models.CharField(
        _('status'),
        max_length=200,
        null=True,
        blank=True, 
    )#override to reduce max_len and remove unique option

    fttd = ArrayField(
        models.CharField(
            max_length=40,
            choices=choices.FAVORITE_THEMES_TO_DISCUSS_CHOICES,
            ),
        null=True, 
        blank=True,
    )#favorite themes to discuss

    fa = ArrayField(
        models.CharField(
            max_length=40,
            choices=choices.FAVORITE_ACTIVITIES_CHOICES,
            ), 
        size=3,
        null=True, 
        blank=True,
    )#favorite activities

    lp = ArrayField(
        models.CharField(
            max_length=40,
            choices=choices.LIFE_PRIORITIES_CHOICES,
            ), 
        null=True, 
        blank=True,
        size=3,
    )#life priorities

    mvpq = ArrayField(
        models.CharField(
            max_length=40,
            choices=choices.MOST_VALUABLE_PERSONAL_QUALITIES_CHOICES,
            ), 
        null=True, 
        blank=True,
        size=3,
    )#most valuable personal qualities

    languages = ArrayField(
        models.CharField(
            max_length=7,
        ),
        null=True,
        blank=True,
    )#languages user knows

    gender = models.CharField(
        max_length=1,
        null=True, 
        blank=True,
        default='n',
    )#user's gender

    dob = models.DateField(
        "Date of birth",
        null=True,
        blank=True
    )#date of birth

    age = models.IntegerField(
        "Age",
        null=True,
        blank=True
    )#age


class UserSettings(models.Model):#defines user's settings for account

    class Meta:
        verbose_name = 'userSettings'
        verbose_name_plural = 'userSettings'

    mainPicture = models.ForeignKey(
        'users.UserPicture',
        on_delete=models.CASCADE,
        related_name='main_For',
        null=True,
    )

    user = models.OneToOneField(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="settings",
    )#user these settings belong to 

    blockedUsers = models.ManyToManyField(
        AUTH_USER_MODEL, 
        related_name="blocked_By",
    )#list of users blocked by this user

    isOpenForNewAcquaintances = models.BooleanField(
        default=True
    )#if True he will be able to use MeetMate accessible via MeetMate

    whoCanSeeMyGeoLocation = models.CharField(
        max_length=6,
    )#who can see country and city 

    whoCanSeeMyAlbums = models.CharField(
        max_length = 6,
        default="all",
    )#everyone can see profile pitcure but user can define who can see other pics


class UserBreakingHistory(BreakingHistory):#responsible for gathering info about user's rule breaking

    class Meta:
        verbose_name = 'UserBreakingHistory'
        verbose_name_plural = 'UserBreakingHistories'
    
    user = models.OneToOneField(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="breaking_History"
    )#user this history belongs to

    thoughUserWasBannedFor = models.ForeignKey(
        "users.Thought",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="thought_User_Was_Banned_For"
    )#if user is banned this thought is shown to him when he tries to login

    nOfSpamComplaints = models.IntegerField(default=0)#how many spam complaints user has received

    lastTimeUserGotSpamComplaint = models.DateField(null=True)#after 1 month of not getting spam complaints nOfSpamComplaints becomes 0 

    nOfSpamBreakings = models.IntegerField(default=0)#how many times user has broken spam rule


class UserAlbum(models.Model):
    
    name = models.CharField(
        max_length=35,
    )#album's name

    description = models.CharField(
        max_length=100,
        null=True,
    )#album's description

    custom = models.BooleanField(
        default=True,
    )#all pictures and thought pictures can not be deleted

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='albums',
    )#user it belongs to

    mainPicture = models.ForeignKey(
        "users.UserPicture",
        on_delete=models.SET_NULL,
        null=True,
        related_name='album_Main_For',
    )#picture which is "face" of the album


class UserPicture(models.Model):

    album = models.ForeignKey(
        "users.UserAlbum",
        on_delete=models.CASCADE,
        related_name="pictures"
    )#album it belongs to

    uploadTime = models.DateTimeField(
        default=timezone.now,
    )#when picture was uploaded    

    picture = models.ImageField(
        upload_to="pics"
    )#picture itself


class Thought(Note):#core value unit created by user
    
    class Meta:
        verbose_name = 'thought'
        verbose_name_plural = 'thoughts'

    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="thoughts",
    )#user this thought belongs to

    pictures = models.ManyToManyField(
        'users.UserPicture',
        related_name="attached_To"
    )#picturse attached to the thought
