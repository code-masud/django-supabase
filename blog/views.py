from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.conf import settings

from .forms import DocumentForm


class HomeView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['form'] = DocumentForm()
        return context


def file_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        fs = FileSystemStorage(
            location=f'{settings.MEDIA_ROOT}/custom',
            base_url=f'{settings.MEDIA_URL}custom/'
        )
        file = request.FILES['file']
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
    else:
        file_url = None

    return render(request, 'blog/index.html', {
        'uploaded_file_url': file_url
    })
