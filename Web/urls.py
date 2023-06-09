"""Web URL Configuration

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
from miBlog.views import *
from Account.views import *
from django.conf import settings
from django.conf.urls.static  import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("post/create",AddPost.as_view(),name="add-post"),
    path("post/list",PostList.as_view(),name="post-list"),
    path("post/<pk>/detail",PostDetail.as_view(),name="post-detail"),
    path("post/<pk>/update",UpdatePost.as_view(),name="update-post"),
    path("post/<pk>/delete",DeletePost.as_view(),name="delete-post"),
    path("signup/",SignUp.as_view(),name="signup"),
    path("login/",Login.as_view(),name="login"),
    path("logout/",Logout.as_view(),name="logout"),
    path("profile/create",CreateProfile.as_view(),name="profile-create"),
    path("profile/<pk>/detail",ProfileDetail.as_view(),name="profile-detail"),
    path("profile/<pk>/update",UpdateProfile.as_view(),name="update-profile"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)