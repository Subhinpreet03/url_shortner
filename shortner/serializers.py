# serializers.py
from rest_framework import serializers
from .models import URL, AccessLog

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['original_url', 'short_url', 'created_at', 'expires_at', 'access_count']

class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = ['url', 'accessed_at', 'ip_address']