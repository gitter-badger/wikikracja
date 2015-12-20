from django.db import models

# Create your models here.


class Act(models.Model):
    # take act_title from
    # https://api-v3.mojepanstwo.pl/dane/sejm_druki?conditions[sejm_druki.numer]=3189
    # and then "sejm_druki.tytul"
    act_title = models.CharField(max_length=200)
    # take act_link from
    # https://api-v3.mojepanstwo.pl/dane/sejm_druki?conditions[sejm_druki.numer]=3189
    # and then "mp_url"
    act_link = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.act_link


class PreChoice(models.Model):
    act = models.ForeignKey(Act)
    text = models.CharField(max_length=200)
    count = models.IntegerField(default=0)


class Choice(models.Model):
    act = models.ForeignKey(Act)
    text = models.CharField(max_length=200)
    yes_count = models.IntegerField(default=0)
    no_count = models.IntegerField(default=0)


class EnvoyChoice(models.Model):
    act = models.ForeignKey(Act)
    text = models.CharField(max_length=200)
    yes_count = models.IntegerField(default=0)
    no_count = models.IntegerField(default=0)
