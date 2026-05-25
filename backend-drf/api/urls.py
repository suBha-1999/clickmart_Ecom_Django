from django.urls import path
# here we'll going to separate views based on apps
from users import views as UserViews
#  ------------------- for token / login----------------
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('register/', UserViews.RegisterView.as_view(), name='Register'),

    # for login we'll use token (access token/ refresh token) ------> for that neeed to install #simplejwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #-----access tokens-------
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #----refresh tokens------
]