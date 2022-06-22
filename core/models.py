import email
import profile

from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


class Profile(models.Model):
    SEX_FEMALE = 'Female'
    SEX_MALE = 'Male'
    SEX_UNSURE = 'Intersex'
    IGEMBE_CENTRAL = 'Igembe Central'
    IGEMBE_NORTH = 'Igembe North'
    IGEMBE_SOUTH = 'Igembe South'
    BACHELOR_DEGREE = 'Bachelor Degree'
    CERTIFICATE  = 'Certificate'
    DIPLOMA = 'Diploma'
    MASTERS ='Masters'
    PHD = 'PHD'
    AKIRANGONDU = "Akirang'ondu"
    ANTUBETWE_KIONGO = 'Antubetwe Kiongo'
    ANTUAMBUI = 'Antuambui'
    ATHIRU_RUNJINE = 'Athiru Runjine'
    KABACHI = 'Kabachi'
    NAATHU = 'Naathu'
    NTUNENE = ' Ntunene'
    IGEMBE_EAST = 'Igembe East'
    KANGETA = 'Kangeta'
    NJIA = 'Njia'
    MAUA = 'Maua'
    KEGOI = 'Kegoi'
    ATHIRU_GAITI = 'Athiru Gaiti'
    AKACHIU = 'Akachiu'
    KANUNI = 'Kanuni'

    SEX_OPTIONS = (
        (SEX_FEMALE, 'Female'),
        (SEX_MALE, 'Male'),
        (SEX_UNSURE, 'Uknown'),
    )

    WARD_OPTIONS = (
        (AKIRANGONDU, "Akirang'ondu"),
        (ANTUBETWE_KIONGO, 'Antubetwe Kiongo'),
        (ANTUAMBUI, 'Antuambui'),
        (ATHIRU_RUNJINE, 'Athiru Runjine'),
        (KABACHI, 'Kabachi'),
        (NAATHU, 'Naathu'),
        (NTUNENE, 'Ntunene'),
        (IGEMBE_EAST, 'Igembe East'),
        (KANGETA, 'Kangeta'),
        (NJIA, 'Njia'),
        (MAUA, 'Maua'),
        (KEGOI, 'Kegoi'),
        (ATHIRU_GAITI, 'Athiru Gaiti'),
        (AKACHIU, 'Akachiu'),
        (KANUNI, 'Kanuni'),
    )

    CONSTITUENCY_OPTIONS = [

        (IGEMBE_CENTRAL, 'Igembe Central'),
        (IGEMBE_NORTH, 'Igembe North'),
        (IGEMBE_SOUTH, 'Igembe South')
    ]
    
    LEVEL_OPTIONS = [
        (BACHELOR_DEGREE, 'Bachelor Degree'),
        (CERTIFICATE, 'Certificate'),
        (DIPLOMA, 'Diploma'),
        (MASTERS, 'Masters'),
        (PHD, 'PHD'),
    ]
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=30, default=SEX_MALE, choices=SEX_OPTIONS)
    id_no = models.CharField(unique=True, blank=False,
                             max_length=8, null=False)
    phone_number = models.CharField(
        blank=False, null=False, max_length=10, unique=True)
    email = models.EmailField(max_length=100, blank=True, unique=True)
    ward = models.CharField(max_length=100, default=NTUNENE, choices= WARD_OPTIONS)
    constituences = models.CharField(
        max_length=100, default=IGEMBE_NORTH, choices=CONSTITUENCY_OPTIONS)
    education_level = models.CharField(max_length=100, default=BACHELOR_DEGREE, choices=LEVEL_OPTIONS)
    graduation_year = models.IntegerField(blank=False)
    resume = models.FileField()
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + '' + self.second_name + '' + self.last_name

   

# class Upload(models.Model):

#     upload_file = models.FileField()
#     upload_date = models.DateTimeField(auto_now_add=True)

    