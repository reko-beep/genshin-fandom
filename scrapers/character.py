from __future__ import annotations

from cachetools import Cache
from .base import BaseScraper

from bs4 import BeautifulSoup
import client

from os import getcwd

class CharacterScraper(BaseScraper):

    def __init__(self, client: client.Client, link: str):

        self.folderpath = getcwd()+"/db/characters/"
        self.link = link
        self.client = client
        self.filename = self.client.generate_id(link)+".json"


    

    def scrape(self):
        
        self.__dict__['data'] = {

        }
        
        src = self.client.get_source_code(self.link)
        bs_object = BeautifulSoup(src, 'lxml')

        raise NotImplementedError
        