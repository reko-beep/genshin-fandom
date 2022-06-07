
from sanic_routing import Route
from yarl import URL





class Routes:
    '''
    Class that holds all the 
    Genshin Fandom routes having list of assets
    to scrape details

    '''
    BASE_URL = URL('https://genshin-impact.fandom.com/wiki') 
    CHARACTER = 'Characters/List'
    WEAPON = 'Weapons/List'
    MATERIAL = 'Materials'
    ARTIFACT = 'Artifacts/Sets'
    FOOD = 'Food'
    FURNISHING = 'Furnishings/List'
    NAMECARD = 'Namecards'
    TALENT_MATERIAL = 'Talent_Level-Up_Materials'
    WEAPON_MATERIAL = 'Weapon_Ascension_Materials'
    ELEMENT = 'Elements'
    DOMAINS = 'Domains/List'
    SPIRAL_ABYSS = 'Spiral_Abyss/Floors'

    @classmethod
    def url(cls, link) -> URL:

        """
        makes a complete url
        from attr of Routes provided or if any attribute is mentioned in string
        """
              
        return cls.BASE_URL / link
    

 

gen = Routes.url(Routes.CHARACTER)
print(gen)