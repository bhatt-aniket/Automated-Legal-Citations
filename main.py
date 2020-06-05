#neutral citation
from bs4 import BeautifulSoup
import requests

def auto_neutral_citation(canlii_url):
    # get url to work with Beautiful Soup
    URL = canlii_url
    content = requests.get(URL)
    auto_gen_citation = BeautifulSoup(content.text, 'html.parser')
    #creating the neutral citation
    neutral_citation = str(auto_gen_citation.title).strip('<title>')
    #getting the name of the case (i.e. x v y)
    case_style = str(auto_gen_citation.title)
    case_style = case_style.split()
    case_style = ' '.join(case_style[5:]).split('|')
    case_style = case_style[0].strip()
    #check if case has neutral citaiton (i.e a case after 1998)
    if neutral_citation[:5] > '1998':
        splitted = neutral_citation.split()
        citation = ' '.join(splitted[0:3])
        return case_style + ', ' + citation
    else:
        return("This case does not have a neutral citation")

#example
print(auto_neutral_citation('https://www.canlii.org/en/bc/bcca/doc/2020/2020bcca158/2020bcca158.html'))
