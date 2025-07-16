from django.db import models
from .conf_HR import WORKERS

DWT = 0 # default work time

class ManSchedule(models.Model):

    Day = models.DateField(blank=False)
    first_shift_worker = models.CharField(max_length=64, choices=WORKERS, blank=True)
    first_shift_time = models.FloatField(default=DWT)
    second_shift_worker = models.CharField(max_length=64, choices=WORKERS, blank=True)
    second_shift_time = models.FloatField(default=DWT)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    class Meta:
        abstract = True

class F1Man(ManSchedule):
    class Meta:
        verbose_name = "F1-Man"
        verbose_name_plural = "F1-Man"

class F3Dmg104(ManSchedule):
    class Meta:
        verbose_name = "F3-Dmg104"
        verbose_name_plural = "F3-Dmg104"

class F4Dmg144(ManSchedule):
    class Meta:
        verbose_name = "F4-Dmg144"
        verbose_name_plural = "F4-Dmg144"

class F5Vtc200(ManSchedule):
    class Meta:
        verbose_name = "F5-Vtc200"
        verbose_name_plural = "F5-Vtc200"

class F6Vtc300(ManSchedule):
    class Meta:
        verbose_name = "F6-Vtc300"
        verbose_name_plural = "F6-Vtc300"

class F7Cheto(ManSchedule):
    class Meta:
        verbose_name = "F7-Cheto"
        verbose_name_plural = "F7-Cheto"

class T1Man(ManSchedule):
    class Meta:
        verbose_name = "T1-Man"
        verbose_name_plural = "T1-Man"

class T2Man(ManSchedule):
    class Meta:
        verbose_name = "T2-an"
        verbose_name_plural = "T2-Man"

class T4Fct(ManSchedule):
    class Meta:
        verbose_name = "T4-Fct"
        verbose_name_plural = "T4-Fct"

class T5Okuma(ManSchedule):
    class Meta:
        verbose_name = "T5-Okuma"
        verbose_name_plural = "T5-Okuma"

class T6Integrex(ManSchedule):
    class Meta:
        verbose_name = "T6-ntegrex"
        verbose_name_plural = "T6-Integrex"

class Pily(ManSchedule):
    class Meta:
        verbose_name = "Piły"
        verbose_name_plural = "Piły"


class MainSchedule():
    pass





















