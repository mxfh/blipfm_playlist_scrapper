import scraperwiki
import lxml.html
import sys
url = "http://blip.fm/profile/diskurs/playlist"
html = scraperwiki.scrape(url)
doc = lxml.html.fromstring(html)
i = 0

for el in doc.cssselect("a.blipTypeIcon"):
    song = el.attrib['title'].replace("\\'", "'").replace("search for ","").encode('utf-8')
    print song
    data = {
        'row': i,
        'song': song
    }
    scraperwiki.sqlite.save(unique_keys=['row'], data=data)
    i+=1
