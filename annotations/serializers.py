from rest_framework import serializers
from .models import Annotation
from django.contrib.auth.models import User

from rest_framework.response import Response

class AnnotationSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True, default=None)
    text = serializers.CharField(required=False, allow_null=True, default='nothing')

    def validate_user(self, value):
        return self.context['request'].user

    class Meta:
        model = Annotation
        fields = ('id', 'user', 'start_time', 'end_time', 'text')


