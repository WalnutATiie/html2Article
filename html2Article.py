#!/usr/bin/env python
# encoding: utf-8
import sys
from htmlGetter import HtmlGetter 
from pattern.web import plaintext
class Html2Article:
    def __init__(self):
        pass
    def html_2_Plaintext(self,html):
        text = plaintext(html,keep=[],replace='',linebreaks=1, indentation=False)
        print text
if __name__ =="__main__":
    H = HtmlGetter()
    html = H.get_html_from_url(sys.argv[1])
    m = Html2Article()
    m.html_2_Plaintext(html)
