from members.serializers import UserSerializer, NewUserSerializer, GameSerializer
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from members.models import Member, Game
import requests, json


class MemberViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        ip = self.request.META['REMOTE_ADDR']
        _user = Member.objects.get(id=self.request.user.id)
        _user.ip_address = ip

        if _user.ip_information:
            pass
        else:
            r = requests.get(f'http://ip-api.com/json/{ip}')
            _user.ip_information = json.loads(r.text)
        
        _user.save()

        if self.action == 'create':
            return NewUserSerializer
        return UserSerializer
    
    @action(detail=True, methods=['GET'])
    def by_token(self, request, pk=None):
        if pk is not None:
            instance = Token.objects.get(key=pk) # TODO: This is throwing a pylint error, by pylint is fucking wrong. Figure this out later.
            user = Member.objects.get(id=instance.user_id)
            serializer = UserSerializer(instance=user)

            return Response(serializer.data)


class GameViewset(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer