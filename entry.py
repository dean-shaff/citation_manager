# -*- coding: utf-8 -*-
import json
from bs4 import BeautifulSoup 
import urllib
import time 
import sys 
reload(sys)
sys.setdefaultencoding('utf8')

class Entry(object):
    """
    A class that represents an entry in a citation database. 
    """
    def __init__(self,*args, **kwargs):
        """
        Create an entry for a paper.
        kwargs:
            - bibtex: raw bibtex data (str)
            - arxiv_url: url from the arxiv
            - author: Author entry (str or list of str) 
            - title: Title entry (str) 
            - year: year published (int or str)
            - journal: name of journal 
            - organization: main organization of authors (str or list of str) 
            - note: A note in markdown about the article 
        """
        self.bibtex = kwargs.get('bibtex',None)
        self.arxiv_url = kwargs.get('arxiv_url',None) 
        if self.bibtex != None:
            self.entry_info = self.process_bibtex(self.bibtex)

        if self.arxiv_url != None:
            self.entry_info, self.bibtext = self.process_arxiv_url(self.arxiv_url,get_bibtex=True) 
        if not self.bibtex and not self.arxiv_url:
            self.entry_info = kwargs

        for key in self.entry_info:
            if not isinstance(self.entry_info[key], list):
                self.entry_info[key] = [self.entry_info[key]]
            
    def __getattr__(self, key):
        
        try:
            return self.entry_info[key] 
        except KeyError:
            return None

    def __str__(self):
        
        auth = self.author_str()
        return "{} by {}".format(self.title[0], auth)

    def process_bibtex(self, bibtex):
        """
        Given some bibtex string, process it and get useful information.
        """
        pass

    def gen_soup(self, url):
        """
        Given some url, generate a soup object from the html file from that url.
        """
        t0 = time.time()
        data = urllib.urlopen(url).read()
        soup = BeautifulSoup(data, 'html.parser')
        print("Took {:4f} seconds to retrieve html for url: {}".format(time.time() - t0, url))
        return soup 

    def process_arxiv_url(self, url, get_bibtex=True):
        """
        Given the url of an arxiv article, get the information about the article. 
        """
        soup = self.gen_soup(url)
        entry_info = {'author':[], 'year':[], 'title':[], 'arxiv_id':[]}
        for item in soup.find_all('meta'):
            if (item['name'] == 'citation_title'):
                entry_info['title'].append(item['content'])
            elif (item['name'] == 'citation_author'):
                entry_info['author'].append(item['content'])
            elif (item['name'] == 'citation_date'):
                entry_info['year'].append(item['content'])
            elif (item['name'] == 'citation_arxiv_id'):
                entry_info['arxiv_id'].append(item['content'])
        
        if get_bibtex:
            for item in soup.find_all('a'):
                if (item.text == "NASA ADS"):
                    ads_url = item.attrs['href'] 
                    break 
            soup_ads = self.gen_soup(ads_url)
            for item in soup_ads.find_all('a'):
                if ("Bibtex" in item.text):
                    bibtex_url = item.attrs['href']
                    break
            html_bibtex = urllib.urlopen(bibtex_url).read()
            index_at = html_bibtex.index('@')
            bibtex = html_bibtex[index_at:]
            print("Successfully scraped the bibtex entry")
            return entry_info, bibtex
        else:
            return entry_info


    def author_str(self):
        """
        create a string that contains the authors names. 
        """
        def reorder_name(name):
            if "," in name:
                name = " ".join(name.split(", ")[::-1]) 
                return name 
            else:
                return name 
        
        authors = [reorder_name(name) for name in self.entry_info['author']]
        if (len(authors) == 1):
            return authors[0] 
        elif (len(authors) == 2):
            return "{} and {}".format(authors[0], authors[1])
        elif (len(authors) > 2):
            auth_str = ", ".join(authors[:-1])
            auth_str += ", and {}".format(authors[-1])
            return auth_str

    def find_keyword(self, keyword,**kwargs):
        """
        Given a keyword, see if it is any of the info about the entry 
        """
        result = False 
        for key in self.entry_info:
            for info in self.entry_info[key]:
                if keyword.lower() in info.lower():
                    result = True 
                    
        return result
               
    def update_note(self, note):
        """
        Update the note associated with the entry. 
        """
        self.entry_info['note'] = [note]

    def create_json(self):
        """
        Turn the entry into json data which can be stored. 
        """
        json_info = json.dumps(self.entry_info)
        return json_info

    def create_bibtex(self):
        """
        Create a bibtex entry from the entry data 
        """
        pass

if __name__ == '__main__':
    e = Entry(arxiv_url="https://arxiv.org/abs/1512.01655")
    print(e) 


