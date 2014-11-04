#!/usr/bin/env python
import scraperwiki
import lxml.html
sivu = 1
while (sivu < 11):
    url = 'http://www.ksml.fi/erikoissivut/verotiedot/suomi/?page=' + str(sivu)
    html = scraperwiki.scrape(url)
    sivu = sivu + 1
    root = lxml.html.fromstring(html)
    for tr in root.cssselect("div[class='table-responsive'] tr"):
        tds = tr.cssselect("td")
        if len(tds)==9:
            data = {
                'sija' : int(tds[0].text_content()),
                'nimi' : tds[1].text_content(),
                'syntymavuosi' : int(tds[2].text_content()),
                'maakunta' : tds[3].text_content(),
                'kokonaistulot' : (tds[4].text_content()),
                'ansiotulot' : (tds[5].text_content()),
                'paaomatulot' : (tds[6].text_content()),
                'veroprosentti' : tds[7].text_content(),
                'tulot_veron_jalkeen' : (tds[8].text_content())
                }
            #print data
            scraperwiki.sql.save(unique_keys=['sija'], data=data)
            

