from rest_framework import serializers
from Planner.models import ItemsToPlan

class ItemsToPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsToPlan
        fields = '__all__'
