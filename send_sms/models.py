from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class contacts(models.Model):
    user = models.ForeignKey(User)
    firstName = models.CharField("Prenom", max_length=20, null=False, blank=False)
    lastName = models.CharField("Nom de Famille", max_length=20, null=True, blank=True)
    phoneNumber = models.CharField("Numero de Telephone", max_length=8, null=True,)

    def __unicode__(self):
        return self.firstName+' '+self.lastName+' - '+self.phoneNumber


class device(models.Model):
    user = models.ForeignKey(User, default=0)
    deviceID = models.IntegerField(max_length=4)
    phoneNumber = models.CharField(max_length=8)
    accountEmail = models.CharField(max_length=30)
    accountPassword = models.CharField(max_length=30)

    def __unicode__(self):
        return self.user.username


class contactgroup(models.Model):
    user = models.ForeignKey(User)
    groupName = models.CharField("Nom du Groupe", max_length=50)
    contact = models.ManyToManyField(contacts)

    def __unicode__(self):
        return self.groupName


class msgTemplates(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField("Le Nom du Template", max_length=20)
    msgText = models.CharField("Modeles de Texte", max_length=160)

    def __unicode__(self):
        return self.name


class message(models.Model):
    user = models.ForeignKey(User)
    sentTo = models.CharField(max_length=10, null=False, blank=False)
    msgText = models.TextField(null=False, blank=False)

    def __unicode__(self):
        return self.user.username


USER_TYPES = ((0, 'Admin'), (1, 'Sub User'))
class userType(models.Model):
    user = models.ForeignKey(User)
    userType = models.IntegerField(choices=USER_TYPES, default=1)

    def __unicode__(self):
        return self.user.username

class adminUser(models.Model):
    masterUser = models.ForeignKey(User, related_name='Master')
    subUser = models.ManyToManyField(User, related_name='Sub')

    def __unicode__(self):
        return self.masterUser.username
