from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from training.models import UserActivity, Activity
from training.serializers import UserActivitySerializer, ActivitySerializer


# Create your views here.

class UserActivityAPIView(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserActivitySerializer
    queryset = UserActivity.objects.none()

    def get_queryset(self):
        # if self.request.user.is_staff:
        #     return UserActivity.objects.all()
        # return UserActivity.objects.filter(user=self.request.user)
        return UserActivity.objects.all()


class ActivityAPIView(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
