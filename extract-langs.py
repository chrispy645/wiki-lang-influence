#!/usr/bin/python

from cz import cz
import sys
import re

f = open("list_lang.html")
body = f.read()
f.close()

body = cz.getbetween2(body, '<td style="width: 33.33%;" align="left" valign="top">\n<ul>', '</ul>\n</td>')

for elem in body:
	split = elem.split('\n')
	for s in split:
		x = cz.getbetween2(s, '<li><a href="', '"')
		if len(x) > 0:
			print "http://en.wikipedia.org" + x[0]
	