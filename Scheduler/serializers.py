from rest_framework import serializers

from Scheduler import *
from Scheduler.models import F1Man


class F1ManSerializer(serializers.ModelSerializer):
    class Meta:
        model = F1Man
        fields = '__all__'
