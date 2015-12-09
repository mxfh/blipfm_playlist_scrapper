#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scraperwiki
import lxml.html
import sys
url = "http://blip.fm/profile/diskurs/playlist"
html = scraperwiki.scrape(url)
doc = lxml.html.fromstring(html)
i = 0

for el in doc.cssselect("a.blipTypeIcon"):
    song = el.attrib['title'].replace("\\'", "'").replace("search for ","")
    songU = song.encode('utf8')
    print songU
    data = {
        'row': i,
        'song': song
    }
    scraperwiki.sqlite.save(unique_keys=['row'], data=data)
    i+=1
