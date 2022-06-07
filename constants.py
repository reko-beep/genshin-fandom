from yarl import URL

class Extend():
    '''
    Class

    easy way to extend the base url i guess without having to write long code for each

    Attrs:

    url -> return yarl URL object
    '''
    BASE_URL = URL('https://genshin-impact.fandom.com/wiki') 

    def __init__(self, name) -> URL:
        self.url = Extend.BASE_URL / name

    def __repr__(self) -> str:
        return self.url

'''

Genshin Fandom all base urls
that will be used to fetch all assets data


'''


CHARACTER = Extend('Characters/List')
WEAPON = Extend('Weapons/List')
MATERIAL = Extend('Materials')
ARTIFACT = Extend('Artifacts/Sets')
FOOD = Extend('Food')
FURNISHING = Extend('Furnishings/List')
NAMECARD = Extend('Namecards')
TALENT_MATERIAL = Extend('Talent_Level-Up_Materials')
WEAPON_MATERIAL = Extend('Weapon_Ascension_Materials')
ELEMENT = Extend('Elements')
DOMAINS = Extend('Domains/List') 
SPIRAL_ABYSS = Extend('Spiral_Abyss/Floors')

