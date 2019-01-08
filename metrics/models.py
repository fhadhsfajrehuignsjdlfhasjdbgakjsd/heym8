from django.db import models
#you need to delete overdue thoughts when gathering day metrics
class DayMetrics(models.Model):

    class Meta:
        verbose_name = 'dayMetrics'
        verbose_name_plural = 'dayMetrics'

    date = models.DateField(

    )#day of measurement

    dayGrowth = models.FloatField(
        
    )#(today total - yesterday total) / yesterday total * 100

    totalUsers = models.IntegerField(

    )#number of undeleted accounts

    activeUsersPercentage = models.IntegerField(

    )#number of active accounts / total users * 100

    usersRegisteredToday = models.IntegerField(

    )#today total - yesterday total

    succesfulMeetMates = models.IntegerField(

    )#today's MeetMates which conversations ended in more than 20 messages

    thoughtsNumber = models.IntegerField(

    )#number of thoughts published today

    MeetMateQuality = models.IntegerField(

    )#today's succesful MeetMates / today's total MeetMates * 100

    MeetMatePerActiveUser = models.IntegerField(

    )#today's n of MeetMate usages / n of active users 

    RateMatePerActiveUsre = models.IntegerField(

    )#today's n of RateMate usages / n of active users

    ThoughtPerAvtiveUser = models.IntegerField(

    )#today's n of thoughts / n of active users



class WeekMetrics(models.Model):
    
    class Meta:
        verbose_name = 'weekMetrics'
        verbose_name_plural = 'weekMetrics'

    date = models.DateField(

    )#day of measurement

    weekGrowth = models.FloatField(
        
    )#(today total - last metrics' total) / last metrics' total * 100

    totalUsers = models.IntegerField(

    )#number of undeleted accounts

    activeUsersPercentage = models.IntegerField(

    )#number of active accounts / total users * 100

    usersRegisteredThisWeek = models.IntegerField(

    )#this metrics' total - last metrics' total

    MeetMateQuality = models.IntegerField(

    )#sum of this week's days succesful MeetMates / sum of this week's days total MeetMates * 100

    MeetMatePerActiveUser = models.IntegerField(

    )#this week's days n of MeetMate usages / n of active users 

    RateMatePerActiveUsre = models.IntegerField(

    )#this week's days n of RateMate usages / n of active users

    ThoughtPerAvtiveUser = models.IntegerField(

    )#this week's days n of thoughts / n of active users


class MonthMetrics(models.Model):

    class Meta:
        verbose_name = 'monthMetrics'
        verbose_name_plural = 'monthMetrics'

    date = models.DateField(

    )#day of measurement

    monthGrowth = models.FloatField(
        
    )#(today total - last metrics' total) / last metrics' total * 100

    totalUsers = models.IntegerField(

    )#number of undeleted accounts

    activeUsersPercentage = models.IntegerField(

    )#number of active accounts / total users * 100

    usersRegisteredThisMonth = models.IntegerField(

    )#this metrics' total - last metrics' total

    MeetMateQuality = models.IntegerField(

    )#sum of this month's days succesful MeetMates / sum of this month's days total MeetMates * 100

    MeetMatePerActiveUser = models.IntegerField(

    )#this month's days n of MeetMate usages / n of active users 

    RateMatePerActiveUsre = models.IntegerField(

    )#this month's days n of RateMate usages / n of active users

    ThoughtPerAvtiveUser = models.IntegerField(

    )#this month's days n of thoughts / n of active users
