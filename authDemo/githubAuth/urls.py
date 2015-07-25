
from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.loginView ),
#	url(r'github/',include('social.apps.django_app.urls', namespace='social'),
	url(r'github/callback',views.githubCallbackView),

]

