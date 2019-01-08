from django.db import models
from HeyM8.settings import AUTH_USER_MODEL


class UserAssessment(models.Model):#one assessment given from one user to another
    
    class Meta:
        verbose_name = 'userAssessment'
        verbose_name_plural = 'userAssessments'

    sender = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_assessments"
    )     

    receiver = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_assessments"
    )

    erudition = models.IntegerField(

    )#erudition assessment

    candor = models.IntegerField(
        
    )#candor assessment

    charisma = models.IntegerField(
        
    )#charisma assessment

    senseOfHumour = models.IntegerField(
        
    )#sense of humour assessment
