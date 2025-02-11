"""ClimbingSocialMedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name="Register"),
    path('',views.auth_login,name = "Login"),
    path('tos/',views.tos,name="TOS"),
    path('post/',views.posts,name="Post"),
    path('post/:likes', views.update_post_likes),
    path('report/',views.report,name="Report"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile, name="Profile"),
    path('profile/<username>', views.profile_other),
    path('user/:following', views.update_followers),
    path('info/',views.per_info,name='PersonalInfo')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
