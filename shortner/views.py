from django.shortcuts import redirect
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import URL, AccessLog
from .serializers import URLSerializer
from datetime import datetime, timedelta
from django.utils import timezone


class ShortenURLView(APIView):
    def post(self, request):
        data = request.data
        original_url = data.get('original_url')
        expiry_hours = data.get('expiry_hours', 24)  # Default to 24 hours

        # Validate URL
        if not original_url:
            return Response({"error": "Original URL is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Create or retrieve the short URL
        url, created = URL.objects.get_or_create(
            original_url=original_url,
            defaults={
                'expires_at': datetime.now() + timedelta(hours=expiry_hours)
            }
        )

        serializer = URLSerializer(url)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

class RedirectView(APIView):
    def get(self, request, short_url):
        try:
            url = URL.objects.get(short_url=short_url)

            # Check expiration
            if url.expires_at < timezone.now():
                return Response({"error": "This URL has expired."}, status=status.HTTP_410_GONE)

            # Log the access
            AccessLog.objects.create(url=url, ip_address=self.get_client_ip(request))

            # Increment access count
            url.access_count += 1
            url.save()

            return redirect(url.original_url)
        except URL.DoesNotExist:
            return Response({"error": "Short URL not found."}, status=status.HTTP_404_NOT_FOUND)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')

class AnalyticsView(APIView):
    def get(self, request, short_url):
        try:
            url = URL.objects.get(short_url=short_url)
            logs = url.access_logs.all()
            data = {
                "original_url": url.original_url,
                "short_url": url.short_url,
                "access_count": url.access_count,
                "logs": [{
                    "accessed_at": log.accessed_at,
                    "ip_address": log.ip_address
                } for log in logs]
            }
            return Response(data)
        except URL.DoesNotExist:
            return Response({"error": "Short URL not found."}, status=status.HTTP_404_NOT_FOUND)
