from django.shortcuts import render
from django.views import View

from .forms import UrlShortnerGetForm, UrlShortnerGetUrl, UrlShortnerCreateUrl
from .logic_layer import Logic


# Create your views here.


class IndexView(View):
    def get(self, request):
        form = UrlShortnerGetForm({'offset': request.GET.get('offset')})
        if form.is_valid():
            result = Logic.get_urls(offset=form.cleaned_data['offset'])
            return render(request=request,
                          template_name='index.html',
                          context={
                              'urls': result
                          })
        pass


class GetUrlView(View):
    def get(self, request):
        form = UrlShortnerGetUrl({'id': request.GET.get('id')})


class CreateUrlView(View):
    def post(self, request):
        form = UrlShortnerCreateUrl({'url': request.POST.get('url')})
        if form.is_valid():
            result = Logic.create_url(url=form.cleaned_data['url'])
        return
