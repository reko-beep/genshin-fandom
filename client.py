
from distutils.command.clean import clean
import typing

from requests_cache import CachedSession
from datetime import timedelta

from yarl import URL
from constants import SCRAPERS
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


    def generate_id(self, string: str) -> str:
        '''

        Generates id from a string
        useful to compare items 

        '''
        seperators = [',','.','/','\\',':',';','-','`','~',"'",'"', '%20', '%27','%22', '%']

        for sep in seperators:
            string = string.replace(sep, '', 99)
        
        return string.lower().replace(' ', '_',99)
    

    def search(self, string: str, strings_list: str, one_result: bool = False, split_search: bool = False) -> typing.Union[str, list]:
        '''
        Searches a string in strings list provided
        returns none if nothing is found
        '''

        results = []

        string = string.lower()
        for item in strings_list:
            splitted = string.split(" ") if split_search else  [string]
            for string_provided in splitted:
                if string_provided in item.lower():
                    results.append(item)
        
        if len(results) == 0:
            return None
        return results[0] if one_result else results

    def get_source_code(self, link: URL):

        '''
        gets source code of the page
        '''

        return self.session.get(link).content
    

    def _get_scraper(self,
                     name: str):

        scraper =  SCRAPERS.get(name)
        return scraper


