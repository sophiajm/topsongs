import scrapy
from songs.items import SongsItem, ErrorItem
from songs.input import getsong, getsonglist
import re

class Songs(scrapy.Spider):
    name = "get-lyrics"
    # allowed_domains = ["https://genius.com/"]

    songdic = getsonglist()
    songlist = list(songdic.keys())
    artistsong = songlist[0]

    songurl = "https://genius.com/"+artistsong+"-lyrics"

    start_urls = [songurl]

    def parse(self, response):
        self.logger.info('\n------hello, just here to get some lyrics')

        songlist = getsonglist()

        for artistsong in songlist:
            songurl = "https://genius.com/"+artistsong+"-lyrics"

            yield scrapy.Request(songurl, callback=self.parse_dir_contents, dont_filter=True)

    def parse_dir_contents(self, response):
        self.logger.info('Parse-dir-contents function called on {}'.format(response.url))

        if response.status == 404:
            self.logger.info("LYRICS NOT FOUND ERROR ERROR")

            item = ErrorItem()
            item['title'] = response.url[19:]
            item['artist'] = response.url[19:]
            item['lyric'] = "ERROR COULD NOT FIND LYRICS"
            item['language'] = self.songdic[response.url[19:-7]][2]
            item['songlink'] = response.url
            yield item

        else:
            lyrics = response.css("div.lyrics > p > a::text").getall() + response.css("div.lyrics > p::text").getall()
            for i,lyrs in enumerate(lyrics):
                lyrics[i] = lyrics[i].strip()
                # lyrics[i] = re.sub(r'\[.*?\]\ *','',lyrics[i])
            lyrics = [lyr for lyr in lyrics if lyr]

            full_lyrics = ' '.join(lyrics)

            item = SongsItem()
            item['title'] = response.css("div.header_with_cover_art-primary_info > h1::text").extract()[0].strip()
            item['artist'] = response.css("div.header_with_cover_art-primary_info > h2 > a::text").extract()[0].strip()
            item['lyric'] = full_lyrics
            item['language'] = self.songdic[response.url[19:-7]][2]
            item['songlink'] = response.url

            yield item

## cd C:\Users\sophiajlm\Documents\DataScience_Projects\03_TopSongsWords\songs
## to run in cmd: scrapy crawl get-lyrics -o outfilename.csv
