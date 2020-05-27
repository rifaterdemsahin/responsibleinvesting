#!python
import json
from urllib.request import urlopen, Request
import urllib
import re


def sendPortfolioToDiscord(event, context):
    url = 'https://www.etoro.com/people/rifaterdemsahin?utm_medium=Direct&utm_source=55714&utm_content=0&utm_serial=SocialShareUrlcopyLink_11356642&utm_campaign=SocialShareUrlcopyLink_11356642&utm_term='
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    
    req = Request(url=url, headers=headers) 
    html = urlopen(req).read().decode('utf-8') 
    text_filtered = re.sub(r'<(.*?)>', '', html)
    
    print(html)

#this output has an iframe in it so it is not useful we need to wait for the api





