#!/usr/bin/env python
# coding:utf-8

import urllib2
import re #Regular Expressions

VideoList=[]

#Use "+" to separate two or more querys(perguntas) , not space
Query='TheRegRunner+Python'
k=0
for html in urllib2.urlopen('http://www.youtube.com/results?search_query='+Query):
	Video=re.search('watch..=...........',html)
	if Video:
		if not Video.group() in VideoList:
			if not '__video_enc' in Video.group():
				VideoList.append(Video.group())
				print VideoList[k]
				k=k+1

for Video in VideoList:
	print 'http://www.youtube.com/'+Video