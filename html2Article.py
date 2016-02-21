#!/usr/bin/env python
# encoding: utf-8
import sys
import re
from htmlGetter import HtmlGetter 
from pattern.web import plaintext
class Html2Article:
    def __init__(self):
        pass
    def html_2_Plaintext(self,html):
        #text = re.sub(r"(?is)<.*?>","",html)
        text = plaintext(html,keep=[],replace='',linebreaks=1, indentation=False)
        #print text
	return text
if __name__ =="__main__":
    H = HtmlGetter()
    html = H.get_html_from_url(sys.argv[1])
    m = Html2Article()
    print m.html_2_Plaintext(html)
