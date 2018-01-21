from .models import Url
from .data_layer import Data


# This layer is meant to be buisness-logic checks. It doesn't care about how we get data

class Logic:

    @staticmethod
    def get_urls(offset):
        urls_data = Data.get_urls_list(offset=offset)  # simple list of dicts, no framework-related objects!
        return urls_data
    
    @staticmethod
    def get_url(url_id):
        url_data = Data.get_url(url_id=url_id)
        return url_data
    
    @staticmethod
    def increase_views(url_id):
        url_data = Data.increase_views(url_id=url_id)
        return url_data
    
    @staticmethod
    def create_url(url):
        url_data = Data.create_url(url=url)
        return url_data