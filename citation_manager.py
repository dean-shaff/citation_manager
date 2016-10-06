from entry import Entry
import markdown2
import json 
import time 

class Citation_Manager(object):
    """
    A class that represents a manager for citations. 
    """
    def __init__(self,**kwargs):
        """
        Initialize the ciation manager. 
        kwargs:
            - entries: a list of citations, either as Python dictionaries
                    or Entry Ojects
        """
        self.entries = kwargs.get('entries', [])
        json_file = kwargs.get('json_file',None)    
        if json_file:
            self.load_json_file(json_file) 

    def load_json_file(self, json_file):
        """
        Load citations in from a json file.
        """
        with open(json_file, 'r') as jsoner:
            entries = json.load(jsoner)
        self.entries = [Entry(**e) for e in entries] 

    def add_entry(self, entry):
        """
        Add an entry or entries to the master entries list
        """
        if (isinstance(entry, list)):
            for e in entry:
                if (isinstance(e, dict)):
                    self.entries.append(Entry(**e))
                else:
                    self.entries.append(e)
        else:
            if (isinstance(entry, dict)):
                self.entries.append(Entry(**entry))
            else:
                self.entries.append(entry) 

    def search(self, keyword):
        """
        Search all the entries in a 
        """
        for e in self.entries:
            result = e.find_keyword(keyword) 
            if result:
                print(e) 

    def render_md(self, save=False, **kwargs):
        """
        Create a valid markdown and html file from the note information from the entries.
        What's cool about this is that it allows us to write mathematical expressions, 
        as well as code (with appropriate syntax highlighting). 
        """
        css_loc = kwargs.get('css_loc','./')
        js_loc = kwargs.get('js_loc','./')
        md = '''<script type="text/x-mathjax-config">
          MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
          </script>\n'''
        md += '''<script type="text/javascript" async
            src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML">
            </script>\n'''
        # md += '''<script type="text/javascript" src="{}MathJax.js"'''.format(js_loc)
        md += '''<link rel="stylesheet" type="text/css" href="{}default.css">\n'''.format(css_loc)
        for e in self.entries:
            md += "## {}\n".format(e.title[0])
            md += "### {}\n".format(e.author_str())
            md += "{}\n\n".format(e.note[0])
        #md += "\n```python\ndef f(x):\n\treturn x**2\n```"
        html = markdown2.markdown(md, extras=['fenced-code-blocks']) 
        if save:
            with open('Citations.md','w') as f_md, open('Citations.html','w') as f_html:
                f_md.write(md) 
                f_html.write(html) 
        else:
            pass

        return md, html
    
    def create_json(self, filename):
        """
        Create a json file with all the citation information. 
        """
        t0 = time.time()
        json_str = "[" 
        for e in self.entries[:-1]:
            json_str += e.create_json()
            json_str += ",\n"
        json_str += self.entries[-1].create_json()
        json_str += "]"
        with open(filename, 'w') as jsoner:
            jsoner.write(json_str) 

        print("Took {:.4f} seconds to generate JSON file".format(time.time() - t0)) 
            
    def __iter__(self):
        """
        Get an iterator 
        """
        for cit in self.entries:
            yield cit

    def __getitem__(self, index):
        return self.entries[index]

if __name__ == '__main__':

    cm = Citation_Manager(json_file='citations_keep.json')
    #cm = Citation_Manager()
    #eSNE = Entry(**{'author':["Geoffrey Hinton","Sam Roweis"],'title':'Stochastic Neighbor Embedding','org':'University of Toronto'})
    #eSNE.update_note("This article is about Stochastic Neighbor embedding.") 
    #etSNE = Entry(**{'author':["Geoffrey Hinton","Laurens van der Maaten"],'title':"Visualizing Data using t-SNE",'org':'University of Toronto','year':2008})
    #etSNE.update_note("This article is about t-distributed Stochastic Neighbor embedding. It's like SNE's better, bigger brother")  

    #cm.add_entry(eSNE)
    #cm.add_entry(etSNE)
    #cm.create_json("citations.json") 
    cm.render_md()
    #cm.search('toronto')
