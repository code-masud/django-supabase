from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext

class HomeView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context
