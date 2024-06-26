"""
https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true
"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        [print(f'-> {attr[0]} > {attr[1]}') for attr in attrs]
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        [print(f'-> {attr[0]} > {attr[1]}') for attr in attrs]

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())