
'''
abc BaseScraper class

All scrapers inherit from this class

'''
from abc import ABC, abstractmethod
from os.path import exists
from os import makedirs, getcwd
from json import load, dump
from typing import TYPE_CHECKING
from munch import Munch, munchify
from datetime import datetime 


class BaseScraper(ABC):
    

    def __init__(self):
        self.update()
        pass


    def create_folder(self, path):
        '''
        
        creates folder

        '''

        try:
            makedirs(path)            
            return True

        except OSError:
            return True
            
    def save(self, data):
        '''
        saves the data into json file     

        ----
        parameters
        ----
        subclass must have 

        filename:  str
        folderpath: str

        '''


        file = self.__dict__.get('folderpath', getcwd()+"/db")+"/"+self.__dict__.get('filename', 'temp.json')
        self.create_folder(file[:file.find(file.split('/')[-1])])

        with open(file, 'r') as f:
            dump(data, f, indent=1)

    

    def update(self):
        '''

        Function that loads the data if it exists else 
        scrapes it from the link using the subclass scrape() function

        ----
        requirements
        ----
        subclass must have 

        filename:  str
        folderpath: str

        '''

        file = self.__dict__.get('folderpath', getcwd()+"/db")+"/"+self.__dict__.get('filename', 'temp.json')
       
        if exists(file):
            data = {}
            with open(file, 'r') as f:
                data = load(f)

            if (datetime.now()-datetime.strptime(data['time'], '%c')).seconds > 3600:

                scrape_func = self.__dict__.get("scrape", None)
                if scrape_func is not None:
                    return scrape_func()     

            else:
                data.pop('time')
                self.__dict__['data'] = munchify(data)

        else:
            scrape_func = self.__getattribute__('scrape')
            if scrape_func is not None:
                return scrape_func()     

    @abstractmethod
    def scrape(self):
        '''
        scraping script in base classes
        '''
        raise NotImplementedError


    @property
    def data(self):
        '''

        returns a munch object of the scraped / fetched data

        '''
        print(self.__dict__)
        checker = self.__dict__.get('data', None)
        if checker is  None:
            return munchify({'error': 'Not yet fetched!'})
        else:
            return munchify(checker)

        
    @property
    def attrs(self):
        '''

        returns list of attrs accessible

        '''
        return [k for k in self.__dict__ if k != 'client']
    
