from django.contrib import admin
from django.conf.urls import url, include

from recipi.web import views


urlpatterns = [
    url(r'^$',
        views.IndexView.as_view(),
        name='recipi-index'),

    url(r'^account/', include('allauth.urls')),

    # Hookup our REST Api
    url(r'^api/', include('recipi.api.urls', namespace='recipi-api')),
    url(r'^api/docs/', include('rest_framework.urls', namespace='rest_framework')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
]
