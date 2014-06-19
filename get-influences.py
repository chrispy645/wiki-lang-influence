#!/usr/bin/python

from cz import cz
import sys
import re
import time
import urllib2

from sys import stdin

def get_langs(st):
	st = "".join(cz.striphtml(st))
	st = re.sub('\\[.*?\\]', '', st).replace('\n', '')
	st = st.split(',')
	st = [ st[0] ] + [ name[1::] for name in st[1::] ]
	return st
	
def fe(arr):
	print ",".join(arr)

for url in stdin.readlines():

	try:

		url = url.rstrip()
		body = cz.geturl(url)
		
		print url[ url.rfind('/')+1 :: ].replace("_(programming_language)","")

		in_by = cz.getbetween2(body, '<th scope="row" style="text-align:left;">Influenced by</th>', '</tr>')
		if len(in_by) > 0:
			in_by = get_langs(in_by[0])
			in_by = [ val.encode('ascii','ignore') for val in in_by ]
			fe(in_by)
		else:
			print
			
		in_to = cz.getbetween2(body, '<th scope="row" style="text-align:left;">Influenced</th>', '</tr>')
		if len(in_to) > 0:
			in_to = get_langs(in_to[0])
			in_to = [ val.encode('ascii','ignore') for val in in_to ]
			fe(in_to)
		else:
			print
			
	except urllib2.HTTPError as e:
		print "DONT_USE"
		print
		print

	time.sleep(0.2)