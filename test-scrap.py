
import requests

from bs4 import BeautifulSoup
URL = 'https://en.wikipedia.org/wiki/Indiana_Jones_and_the_Kingdom_of_the_Crystal_Skull#Cast'
website_url = requests.get(URL).text   
soup = BeautifulSoup(website_url,'lxml')
section = soup.find('span', id='Cast').parent

Stars = []
for x in section.find_next('ul').select('li > a:nth-child(1)'):
        Stars.append(x.get('title'))



""" print(Stars)"""


""" 
URL = 'https://es.wikipedia.org/wiki/18_de_enero'
website_url = requests.get(URL).text   
soup = BeautifulSoup(website_url,'lxml')
section = soup.find('span', id='Acontecimientos').parent

Stars = []
text = []
for x in section.find_next('ul').select('li > a:nth-of-type(1)'):
        Stars.append(x.get('title'))
        Stars.append(x.text)
        
print(Stars)
print(text)
"""


URL = 'https://www.litoralpress.cl/sitio/trendings.cshtml'
website_url = requests.get(URL).text   
soup = BeautifulSoup(website_url,'lxml')
section = soup.find('ul', class_ = 'numeros').parent

lista_trendings = []
for x in section.find_next('ul').select('li'):
        lista_trendings.append(x.get('title'))

print('\n')
print(lista_trendings)
""" print(Stars) """

print('\n')