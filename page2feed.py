#!/usr/bin/env python3

import requests
import sys
from bs4 import BeautifulSoup


for a in sys.stdin:
    line = a.strip().split()
    url = line[0]
    source = line[1]

    end_link_selector = line.index("a") + 1
    link_selector = " ".join(line[2:end_link_selector])
    title_selector = " ".join(line[end_link_selector:])
    
    doc = BeautifulSoup(requests.get(url).text, "html.parser")
    print(source)

    links = [link for link in doc.select(link_selector)]
    titles = [t for t in doc.select(title_selector)]
    
    for l, t in zip(links, titles):
        print("title: ", t)
        print("  link: ", l.get("href"))

