from rest_framework import serializers
from .models import Entry, Partyname, Prices


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Partyname
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = '__all__'
