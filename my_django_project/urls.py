from django.contrib import admin
from django.urls import include, path

from accounts.api.views import IncrementCountView
from accounts.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/me/count', IncrementCountView.as_view(), name='increment_count'),
    path('', HomePageView.as_view(), name='home')
]