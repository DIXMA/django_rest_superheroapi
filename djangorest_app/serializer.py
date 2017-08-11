from rest_framework import serializers
from djangorest_app.models import Publisher, SpuerHero


class SpuerHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpuerHero
        fields = ('id', 'name', 'gender', 'realname', 'publisher')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'founder')
