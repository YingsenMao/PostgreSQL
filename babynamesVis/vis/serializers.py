from rest_framework import serializers
from vis.models import Babynames


class BabyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Babynames
        fields = ('year', 'name', 'n')