from yarl import URL
from importlib import import_module


__all__ = ['CHARACTER', 
            'WEAPON',
            'MATERIAL',
            'ARTIFACT',
            'FOOD',
            'FURNISHING',
            'NAMECARD',
            'TALENT_MATERIAL',
            'WEAPON_MATERIAL',
            'ELEMENT',
            'DOMAINS',
            'SPIRAL_ABYSS']

'''
-------------------

URL CONSTANTS
-----------

'''            


class ExtendURL:
    '''
    ---
    ExtendURL Class
    ---

    easy way to extend the base url i guess without having to write long code for each

    ---
    attrs:
    ---
    url -> return yarl URL object
    
    '''
    BASE_URL = 'https://genshin-impact.fandom.com/wiki/' 

    def __init__(self, name) -> URL:
        if 'wiki' in name:
            name = name.replace("/wiki/",'',1)
        self.url = f'{ExtendURL.BASE_URL}{name}'

    def __repr__(self) -> str:
        return self.url
    
    def __str__(self) -> str:
        return str(self.url)

'''

Genshin Fandom all base urls
that will be used to fetch all assets data


'''


CHARACTER = ExtendURL('Characters/List')
WEAPON = ExtendURL('Weapons/List')
MATERIAL = ExtendURL('Materials')
ARTIFACT = ExtendURL('Artifacts/Sets')
FOOD = ExtendURL('Food')
FURNISHING = ExtendURL('Furnishings/List')
NAMECARD = ExtendURL('Namecards')
TALENT_MATERIAL = ExtendURL('Talent_Level-Up_Materials')
WEAPON_MATERIAL = ExtendURL('Weapon_Ascension_Materials')
ELEMENT = ExtendURL('Elements')
DOMAINS = ExtendURL('Domains/List') 
SPIRAL_ABYSS = ExtendURL('Spiral_Abyss/Floors')

'''

SCRAPER CONSTANTS

'''

class ScraperManager:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)
        self.import_path = '.scrapers.'

    def get(self, name: str):

        '''

        returns the scraper class
        specified

        '''

        if name in self.__dict__:
            module = import_module(f'scrapers.{name}')
            if module:
                return getattr(module, self.__dict__[name])







SCRAPERS = ScraperManager(character='CharacterScraper')



IMG_NOT_FOUND = 'https://bsmedia.business-standard.com/_media/bs/img/about-page/thumb/464_464/1599716993.jpg'
    