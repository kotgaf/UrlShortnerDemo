from django.conf.urls import url

from .views import GetUrlView, CreateUrlView, IndexView
urlpatterns = [
    url('^$', IndexView.as_view())
]