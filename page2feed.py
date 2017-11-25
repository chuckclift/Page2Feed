#!/usr/bin/env python3

import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import urllib
import argparse
import configparser



parser = argparse.ArgumentParser(description="fetch feed from all urls specified in config file")
parser.add_argument("config", help="input config file")
args = parser.parse_args()

config = configparser.RawConfigParser()
config.read(args.config)

for s in config.sections():
    url = config.get(s, "url")
    section_selector = config.get(s, "section")
    link_selector = config.get(s, "link")
    title_selector = config.get(s, "title")

    scheme = urlparse(url).scheme
    host = urlparse(url).netloc
     
    doc = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

    for section in doc.select(section_selector):
        t = section.select(title_selector)[0]
        l = section.select(link_selector)
        for link in l:
            print(link.get("href"), t.get_text())
            
