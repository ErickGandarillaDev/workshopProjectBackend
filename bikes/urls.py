from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('client.urls')),
    path('api/', include('date.urls')),
    path('api/', include('diagnosis.urls')),
    path('api/', include('motorcycle.urls')),
    path('api/', include('status.urls')),
    path('api/', include('RepairSummary.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
