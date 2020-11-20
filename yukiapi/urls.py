from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
from members.views import MemberViewset, GameViewset

router = routers.DefaultRouter()
router.register(r'members', MemberViewset)
router.register(r'games', GameViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
    path (r'api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path(r'api/api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    
]
