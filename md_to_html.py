import markdown2
import sys 

filename = sys.argv[1]
output = sys.argv[2]
with open(filename, 'r') as md, open(output, 'w') as html:
    md_str = md.read() 
    html_str = markdown2.markdown(md_str,extras=['fenced-code-blocks']) 
    html.write(html_str) 



