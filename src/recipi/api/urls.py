from django.conf.urls import url

from recipi.api import endpoints


urlpatterns = [
    url(r'^users/$',
        endpoints.UserListEndpoint.as_view(),
        name='recipi-api-user-list'),
    url(r'^users/(?P<pk>.+)/$',
        endpoints.UserEndpoint.as_view(),
        name='recipi-api-user'),

    url(r'^',
        endpoints.CatchallEndpoint.as_view(),
        name='recipi-api-catchall'),
]
