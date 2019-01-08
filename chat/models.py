from django.db import models
from django.utils.timezone import now
from HeyM8.settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _


class Message(models.Model):

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')

    messageSender = models.ForeignKey(
        AUTH_USER_MODEL,    
        related_name="sent_messages",
        on_delete=models.CASCADE
    )#User who has sent message

    messageReceiver = models.ForeignKey(
        AUTH_USER_MODEL, 
        related_name="received_messages",
        on_delete=models.CASCADE
    )#User who must receive message

    conversation = models.ForeignKey(
        "Conversation",
        on_delete=models.CASCADE, 
        related_name="messages"
    )#Conversation where message takes place

    message_text = models.TextField(max_length=512)

    isRead = models.BooleanField(default=False)#if message is read by receiver

    isDeletedBySender = models.BooleanField(default=False)#if message is deleted by sender

    isDeletedByReceiver = models.BooleanField(default=False)#if message is deleted by receiver

    time = models.DateTimeField(
        "When message was sent"
    )#when message was handled by server


class Conversation(models.Model):

    class Meta:
        verbose_name = _('conversation')
        verbose_name_plural = _('conversations')

    date = models.DateField(

    )#when conversation was started

    foundUsingMeetMate = models.BooleanField(

    )#if conversation was found using MeetMate

    firstMeetMateForOneOfUsers = models.BooleanField(

    )#if foundUsingMeetMate indicates if it is first MeetMate usage for one of users

    messagesTotal = models.BigIntegerField(
        default=0,
    )#number of messages from both users 

    firstConversationUser = models.ForeignKey(
        AUTH_USER_MODEL, 
        related_name="conversations_where_first",
        on_delete=models.CASCADE
    )#first conversation user

    secondConversationUser = models.ForeignKey(
        AUTH_USER_MODEL, 
        related_name="conversations_where_second",
        on_delete=models.CASCADE
    )#second conversation user

    deletedForFirstUser = models.BooleanField(
        default=False,
    )#indicates whether conversation was deleted for first user

    deletedForSecondUser = models.BooleanField(
        default=False,
    )#indicates whether conversation was deleted for second user
