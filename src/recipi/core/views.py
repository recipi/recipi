from django.views.generic import TemplateView
from tumblpy import Tumblpy


class IndexView(TemplateView):
    """View for the index page"""
    template_name = 'recipi/core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        user = self.request.user

        if user.is_authenticated():
            social_account = user.socialaccount_set.get(provider='tumblr')
            social_token = social_account.socialtoken_set.get(app__provider='tumblr')

            tumblr = Tumblpy(
                app_key=social_token.app.client_id,
                app_secret=social_token.app.secret,
                oauth_token=social_token.token,
                oauth_token_secret=social_token.token_secret)

            context['user_info'] = tumblr.post('user/info')
        return context


class EditorView(TemplateView):
    template_name = 'recipi/recipes/editor.html'
