from django.urls import path
from .views import ShortenURLView, RedirectView, AnalyticsView

urlpatterns = [
    path('shorten/', ShortenURLView.as_view(), name='shorten'),
    path('redirect/<str:short_url>/', RedirectView.as_view(), name='redirect'),
    path('analytics/<str:short_url>/', AnalyticsView.as_view(), name='analytics'),
]