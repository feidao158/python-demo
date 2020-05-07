import requests
from bs4 import BeautifulSoup


class html_prase_object:
    @staticmethod
    def get_content(cls):
        res = requests.get(cls)
        if res.status_code == 200:
            return res.content
        else:
            return None
    @staticmethod
    def prase_html(content):
        soup = BeautifulSoup(content,'lxml')
        print(soup)
