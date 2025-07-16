from django.db import models
from Scheduler.models import ManSchedule
from Planner.const import CURSOR, ENGINE
class GeneralPlanner(models.Model):
    id = models.IntegerField(primary_key=True)
    pcs = models.IntegerField()
    start_time = models.DateTimeField()
    duration = models.FloatField()
    end_time = models.TimeField()

    class Meta:
        abstract = True


class PilyPlanner(GeneralPlanner):
    class Meta:
        verbose_name = "PiłyPlanner"
        verbose_name_plural = "PiłyPlanner"

class F1ManPlanner(GeneralPlanner):
    class Meta:
        verbose_name = "F1-Man Planner"
        verbose_name_plural = "F1-Man Planner"

class T1ManPlanner(GeneralPlanner):
    class Meta:
        verbose_name = "T1-Man Planner"
        verbose_name_plural = "T1-Man Planner"


class T2ManPlanner(GeneralPlanner):
    class Meta:
        verbose_name = "T2-Man Planner"
        verbose_name_plural = "T2-Man Planner"


class F3DMG103Planner(GeneralPlanner):
    class Meta:
        verbose_name = "F3-DMG103 Planner"
        verbose_name_plural = "F3-DMG103 Planner"


class F4DMG144Planner(GeneralPlanner):
    class Meta:
        verbose_name = "F4-DMG 144Planner"
        verbose_name_plural = "F4-DMG 144Planner"


class F5MazVTC200Planner(GeneralPlanner):
    class Meta:
        verbose_name = "F5-Maz VTC200 Planner"
        verbose_name_plural = "F5-Maz VT-C200 Planner"


class F6MazVTC300Planner(GeneralPlanner):
    class Meta:
        verbose_name = "F6-Maz VTC300Planner"
        verbose_name_plural = "F6-Maz VTC300Planner"


class F7ChetoPlanner(GeneralPlanner):
    class Meta:
        verbose_name = "F7-Cheto Planner"
        verbose_name_plural = "F7 Cheto Planner"


class ItemsToPlan(models.Model):
    item_id = models.IntegerField(unique=True)
    drawing = models.CharField(max_length=50)
    po = models.IntegerField()
    material = models.CharField(max_length=50)
    comment =  models.CharField(max_length=50)
    przygotowka = models.CharField(max_length=50)
    order_start = models.IntegerField(null=True, blank=True)
    all_operations = models.CharField(max_length=128)
    is_saw = models.BooleanField()
    sawcutting_time = models.FloatField(null=True, blank=True)
    sawcutting_start = models.IntegerField(null=True, blank=True)
    sawcutting_finish = models.IntegerField(null=True, blank=True)
    is_milling = models.BooleanField()
    milling_time = models.FloatField(null=True, blank=True)
    milling_start = models.IntegerField(null=True, blank=True)
    milling_finish = models.IntegerField(null=True, blank=True)
    is_turning = models.BooleanField()
    turning_time = models.FloatField(null=True, blank=True)
    turning_start = models.IntegerField(null=True, blank=True)
    turning_finish = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.po} {self.drawing}'

if __name__ == "__main__":
    pass