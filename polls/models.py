from django.db import models
from django.utils.encoding import python_2_unicode_compatible

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




'''
Musimy zmienić modele tak aby pozwalały na cofnięcie głosu w drugim etapie

1. Zbieranie podpisów pod ustawą.
    Tabela1 zawiera: id druku, numer druku, tytuł ustawy, link do treści, liczbę głosów ZA, guzik do głosowania ZA, znacznik mówiący
    czy przeszła + w widoku guzik do podpisania się (nie można wycofać podpisu).
2. Tabela2 zawierająca sumaryczną liczbę głosów ZA i PRZECIW danej ustawie. A dokładnie:
    data rozpoczęcia głosowania, data zakończenia głosowania, czy głosowanie otwarte (na podstawie dat), id druku (FK),
    liczba głosów ZA, liczba głosów PRZECIW + w widoku guziki ZA, PRZECIW, RESET
3. Tabela3 zawierająca głosy użytkowników OSOBA <> GŁOSOWANIE <> GŁOS
    Tabela zawiera: id druku, id użytkownika, za/przeciw
4. Tabela4 zawierająca głosy posłów. A dokładnie:
    id posła, imię i nazwisko posła, partia posła, ZA czy PRZECIW, id druku, czy głosował zgodnie z naszą wolą

'''
