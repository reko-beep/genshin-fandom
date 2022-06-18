from __future__ import annotations
from typing import TYPE_CHECKING

from .base import BaseScraper

from bs4 import BeautifulSoup
from .utils import generate_id, find_image
from os import getcwd

if TYPE_CHECKING:
    import client
class CharacterScraper(BaseScraper):

    def __init__(self, client: client.Client, link: str):

        self.folderpath = getcwd()+"/db/characters/"
        self.link = link
        self.client = client
        self.filename = generate_id(link.split('/')[-1])+".json"
        super().__init__()
        
    
   


    

    def scrape(self):
        
        self.__dict__['data'] = {

        }
        src = self.client.get_source_code(self.link)
        bs_object = BeautifulSoup(src, 'lxml')

        '''
        Main side bar info

        '''

        main_sb = bs_object.find('aside', {'role': 'region'})

        main_data_sources = [i.attrs['data-source'] for i in main_sb.find_all(attrs={'data-source': True})]
        for ds in main_data_sources:
            element = bs_object.find('div', {'data-source': ds})
            if element is not None:
                value = element.find('div')
                values = 'N/A'

                if value.find('a') is not None and ds not in ['image', 'element', 'region', 'affiliation', 'voiceKR', 'voiceEN', 'voiceJP']:
                    values = [t.text for t in value.find_all('a')]
                else:
                    if ds == 'image':                        
                        self.__dict__['data']['img'] = {}
                        figures = element.find_all('figure')
                        for figure in figures:
                            img = find_image(figure)
                            key = generate_id(figure.find('a').attrs['title'])
                            self.__dict__['data']['img'][key] = img
                    else:
                        values = value.text.strip()
                values = values[0] if len(values) == 1 and type(values) == list else values
                self.__dict__['data'][ds] = values

        