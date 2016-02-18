#!/usr/bin/env python
# encoding: utf-8
import requests
import logging
class HtmlGetter:
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename='html2Article.log',
            filemode='w')
    #@staticmethod    
    def get_html_from_url(self,url):
        try:		
            r = requests.get(url)
	except:
            logging.error("fail to get html from url:%s." % url)
            return None
        else:
            return r.text
if __name__ == "__main__":
    H = HtmlGetter()
    print H.get_html_from_url("http://www.baidu.com")
