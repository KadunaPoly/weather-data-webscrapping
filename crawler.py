#!/usr/local/bin/python3
"""""""""""""""My Frist web Scrapping with Python and BeatyfullSoop"""""""""""""
from bs4 import BeautifulSoup as bs
from urllib.request import Request,urlopen
url = "https://www.sfds.asso.fr/fr/n/506-consulter_les_offres_demploi/?jedu=M
ASTER&jcon=&jp=3"
page = urlopen(url)
html = bs(page, 'html')
print(html)
