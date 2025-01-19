from django.db import models
from hashlib import md5
from datetime import timedelta, datetime


class URL(models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    access_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_url:
            # Generate a hash-based short URL
            self.short_url = md5(self.original_url.encode()).hexdigest()[:10]
        super().save(*args, **kwargs)


class AccessLog(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE, related_name="access_logs")
    accessed_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
