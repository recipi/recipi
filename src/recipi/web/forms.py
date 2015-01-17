import floppyforms.__future__ as forms
from django.utils.translation import ugettext_lazy as _

from recipi.models.user import User


class RegisterForm(forms.ModelForm):
    name = forms.CharField(label=_('Your name'),
        widget=forms.TextInput(
            attrs={'placeholder': _('e.g Jorah Mormont')}))
    email = forms.EmailField(label=_('Email'))

    class Meta:
        model = User
        fields = ('name', 'email')

    def signup(self, request, user):
        user.name = self.instance.name
        user.email = self.instance.email
        user.save()
