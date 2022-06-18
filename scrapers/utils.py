
import typing
from xml.dom.minidom import Element
from bs4 import element
from constants import IMG_NOT_FOUND

def generate_id(string: str) -> str:
        '''

        Generates id from a string
        useful to compare items 

        '''
        seperators = [',','.','/','\\',':',';','-','`','~',"'",'"', '%20', '%27','%22', '%']        
        for sep in seperators:
            string = string.replace(sep, '', 99)
        
        return string.lower().replace(' ', '_',99)
    

def search(string: str, strings_list: str, one_result: bool = False, split_search: bool = False) -> typing.Union[str, list]:
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


def find_image(img: element.Tag):
    '''

    finds image link provided an bs4.element.Tag object

    '''

    element_ = img
    if img.name != 'img':
        element_ = img.find('img')
        if element_ is None:
            return IMG_NOT_FOUND
    
    if 'data-src' in element_.attrs:
        if element_.attrs['data-src'].startswith('http'):
            return element_.attrs['data-src'][:element_.attrs['data-src'].find('/revision')]
    
    if 'src' in element_.attrs:
        if element_.attrs['src'].startswith('http'):
            return element_.attrs['src'][:element_.attrs['src'].find('/revision')]
    
    return IMG_NOT_FOUND