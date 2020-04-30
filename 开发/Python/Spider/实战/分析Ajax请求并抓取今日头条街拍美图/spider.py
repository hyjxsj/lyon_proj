#-*- coding:utf-8 -*-
__author = "Lukas"

import requests
import re
from bs4 import BeautifulSoup

def get_page_index(offset,):
    data = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':3
    }
