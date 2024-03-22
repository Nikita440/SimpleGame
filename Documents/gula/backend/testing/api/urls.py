from django.urls import path

from . import views
from .views import MyTokenObtainPairView, changename

from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)
    
urlpatterns = [
    path('',views.routes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.register,name='user-register'),
    path('getInfo/',views.getuserinfo),
   path('changename/', views.changename, name='changename'),
]
