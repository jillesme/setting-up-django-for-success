from django.contrib import admin
from django.urls import path, include

from accounts.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', HomePageView.as_view(), name='home')
]