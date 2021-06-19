from rest_framework import serializers
from things.models import Thing, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class ThingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='thing-highlight', format='html')

    class Meta:
        model = Thing
        fields = ['url', 'id', 'title', 'owner', 'value1', 'value2', 'value3', 'value4', 'switch1', 'switch2']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    things = serializers.HyperlinkedRelatedField(many=True, view_name='thing-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'things']
