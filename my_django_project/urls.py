from django.contrib import admin
from django.urls import path, include

from accounts.views import HomePageView
from accounts.api.views import IncrementCountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/me/count', IncrementCountView.as_view(), name='increment_count'),
    path('', HomePageView.as_view(), name='home')
]