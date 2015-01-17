from recipi.api.base import Endpoint, ListEndpoint
from recipi.models.user import User
from recipi.serializers.user import UserSerializer


class UserEndpoint(Endpoint):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    http_method_names = ['get']


class UserListEndpoint(UserEndpoint, ListEndpoint):
    pass
