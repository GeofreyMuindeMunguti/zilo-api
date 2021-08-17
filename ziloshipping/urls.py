"""ziloshipping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from users.views import UserRegisterView
#...

auth_urls = [
    url(r'^login/', obtain_jwt_token),
    url(r'^refresh/', refresh_jwt_token),
    url(r'^verify/', verify_jwt_token),
    url(r"^register/", UserRegisterView.as_view(), name="register_user"),
]

v1_urls = [
    url(r"", include("users.urls")),
    url(r"orders/", include("orders.urls")),
    url(r"inventory/", include("inventory.urls")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('browsable/', include('rest_framework.urls')),
    url(r"^auth/", include(auth_urls)),
    url(r"^api/v1/", include(v1_urls)),
]
