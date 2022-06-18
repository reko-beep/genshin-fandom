
from __future__ import annotations
from distutils.command.clean import clean
import typing
from bs4 import BeautifulSoup
from typing import TYPE_CHECKING

from requests_cache import CachedSession
from datetime import timedelta

from yarl import URL
from constants import SCRAPERS, ExtendURL
from constants import *

if TYPE_CHECKING:
    from scrapers.character import CharacterScraper

class Client:
    
    def __init__(self):
        '''
        Initializes the Genshin Fandom client
        '''
        
        self.session = CachedSession(
        'fandomcache',
        use_cache_dir=True,                # Save files in the default user cache dir
        cache_control=True,                # Use Cache-Control headers for expiration, if available
        expire_after=timedelta(days=1),    # Otherwise expire responses after one day
        allowable_methods=['GET', 'POST'], # Cache POST requests to avoid sending the same data twice
        allowable_codes=[200, 400],    # Don't match this param or save it in the cache
        match_headers=True,                # Match all request headers
        stale_if_error=True,               # In case of request errors, use stale cache data if possible
    )

        self.characters = self._character_lists()


    def get_source_code(self, link: URL):
    
        '''
        gets source code of the page
        '''

        return self.session.get(link).content

    

    def get_scraper(self,
                     name: str):
        '''

        Private function of client
        gets the scraper depending on the name

        ----
        parameters
        ----

        name: module name
        '''

        scraper =  SCRAPERS.get(name)
        return scraper

    def get_table(self, bs : BeautifulSoup,
                    id_ : str):

        '''

        Private function of client
        gets the table from Beautiful soup object

        ----
        parameters
        ----

        id_ : id of the h2 element
        '''
        
        table_ = bs.find("span", {"id": id_})
        if table_ is not None:
            element = table_.parent.find_next_sibling()
            while element.name != 'table':
                element = element.find_next_sibling()
            else:
                return element
        return None

    def filter_item(self, 
                        title_string: str, list_: typing.List[BaseItem]):
        '''
        returns a item if it exists

        from list of BaseItem

        ---
        params
        ---
        title_string: title to search for
        list_ : list of BaseItem
        '''
        for item in list_:
            if title_string.lower() in item.title.lower():
                return item


    def _character_lists(self) -> typing.Union[typing.List[BaseItem], None]:
        '''

        fetches all characters list from fandom

        '''
        src = self.get_source_code(CHARACTER)
        bs = BeautifulSoup(src, 'lxml')
        tables = [self.get_table(bs, 'Upcoming_Playable_Characters'), self.get_table(bs, 'Playable_Characters')]
  
        list_ = []        
        for table in tables:
            if table is not None:
                rows = table.find_all('tr')[1:]
                for r in rows:
                    columns = r.find_all('td')
                    if len(columns) >= 5:
                        title = columns[1].text.strip()
                        link = ExtendURL(columns[1].find('a').attrs['href']).url
                        list_.append(BaseItem(client=self, 
                                            title=title,
                                            url=link,
                                            type_module='character'))      

       

        return list_

class BaseItem:
    '''
    BaseItem

    can be anything character, weapon, materials, wishes etc

    '''

    def __init__(self, client: Client, title: str, url: str, type_module: str) -> None:
        self.client = client
        self.title = title
        self.url = url
        self.type_module = type_module

    def __repr__(self) -> str:
        string = ' '.join([f"{k}={self.__dict__[k]}" for k in  self.__dict__])
        return f"<{self.type_module.title()} {string}>"

    def get_data(self) -> CharacterScraper: 
        '''

        Stores | returns the data of a specific item

        you can do .attrs to see available attrs of the object

        .data returns the whole data

        '''

        scraper = self.client.get_scraper(self.type_module)
        if scraper is not None:
            return scraper(self.client, self.url)



test = Client()
test_char_obj = test.filter_item('albedo', test.characters)
albedo_data = test_char_obj.get_data()

