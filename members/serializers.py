from django.core.validators import RegexValidator
from rest_framework import serializers
from members.models import Member, Game

alpha_only = RegexValidator('^[A-Za-z0-9_]+$', message='Alphanumerics only please')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        exclude = ('email', 'password')


class NewUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    twitch = serializers.CharField()
    twitter = serializers.CharField()
    # handle = serializers.CharField()

    def create(self, val_data):
        password = val_data.pop('password', None)
        username = val_data.pop('username', None)
        email = val_data.pop('email', None)
        twitch = val_data.pop('twitch', None)
        twitter = val_data.pop('twitter', None)

        # Check if user exists
        does_exist = Member.objects.filter(username__iexact=username)
        if len(does_exist) > 0:
            return # TODO: This is fucking retarded
        
        user_instance = Member(email=email, username=username, twitch=twitch, twitter=twitter)
        if password is not None: user_instance.set_password(password)
        user_instance.save()

        return user_instance


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'