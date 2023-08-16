#!/usr/bin/env python3
# [P]scra[P] | Coded with <3 by Tanishq Rathore
from bs4 import BeautifulSoup
import requests

def printParams(url):
    sess = requests.Session()
    resp = sess.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    form = soup.find('form')
    if form:
        input_elements = form.find_all('input')
        for input_element in input_elements:
            input_name = input_element.get('name')
            if input_name:
                print(input_name)

