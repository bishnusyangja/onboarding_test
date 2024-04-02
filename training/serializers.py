from django.contrib.auth.models import User
from rest_framework import serializers

from training.models import UserActivity, Activity


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    start_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    end_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Activity
        fields = ('id', 'name', 'description', 'is_active', 'start_date', 'end_date', 'created_at', 'updated_at', )


def key_contains_id(values):
    if 'id' not in values:
        raise serializers.ValidationError('It must contain id as key item.')


class UserActivitySerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    completed = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    user = serializers.DictField(source='user_dict')
    activity = serializers.DictField(source='activity_dict')
    score = serializers.IntegerField(source='get_score')

    class Meta:
        model = UserActivity
        fields = ('id', 'activity','user', 'completed', 'created_at', 'updated_at', 'score', )

    def validate_user(self, attrs):
        key_contains_id(attrs)
        if User.objects.filter(id=attrs['id']).count() < 1:
            raise serializers.ValidationError('Not a valid user id')
        return attrs

    def validate_activity(self, attrs):
        key_contains_id(attrs)
        if Activity.objects.filter(id=attrs['id']).count() < 1:
            raise serializers.ValidationError('Not a valid activity id')
        return attrs

    def create(self, validated_data):
        validated_data['user'] = validated_data['user']['id']
        validated_data['activity'] = validated_data['activity']['id']
        return super(self, validated_data)