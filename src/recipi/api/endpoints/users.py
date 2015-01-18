from recipi.api.base import Endpoint, ListEndpoint
from recipi.api.serializers.user import UserSerializer
from recipi.accounts.models import User


class UserEndpoint(Endpoint):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    http_method_names = ['get']


class UserListEndpoint(UserEndpoint, ListEndpoint):
    pass
