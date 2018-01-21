# Data layer . Here we can retrieve our data from different sources

from .models import Url

class Data:

    @classmethod
    def increase_views(cls, url_id):
        url = Url.objects.get(url_id=url_id)
        url.views += 1
        url.save()
        return cls.convert_urls(urls=[url])

    @classmethod
    def get_url(cls, url_id):
        url = Url.objects.get(id=url_id)
        return cls.convert_urls(urls=[url])

    @classmethod
    def get_urls_list(cls, offset):
        urls = Url.objects.all()[offset:10]
        return cls.convert_urls(urls=urls)

    @classmethod
    def create_url(cls, url):
        url_obj = Url.objects.create(url=url)
        return cls.convert_urls([url_obj])

    @classmethod
    def convert_urls(cls, urls):
        # main point is to strip framework-depended structure, only plain and native objects
        result = []
        for url in urls:
            result.append({
                'id': url.id,
                'short': url.short,
                'created': url.created,
                'views': url.views
            })
        return result
