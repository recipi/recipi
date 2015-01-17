from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RecipiConfig(AppConfig):
    name = 'recipi'
    verbose_name = _('Recipi')

    def ready(self):
        # We do like our application structure more than django's
        # so we import our modules manually.
        from recipi.models import user  # noqa
