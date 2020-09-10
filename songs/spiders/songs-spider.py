import scrapy
# from scrapy.loader import ItemLoader
from songs.items import SongsItem
from songs.input import getsong, getsonglist
import re


## cd C:\Users\sophiajlm\Documents\DataScience_Projects\03_TopSongsWords\songs
## to run in cmd: scrapy crawl get-lyrics -o outfilename.csv

class Songs(scrapy.Spider):
    name = "get-lyrics"
    # allowed_domains = ["https://genius.com/"]
    songlist = getsonglist()
    artistsong = getsong(songlist[0])
    songurl = "https://genius.com/"+artistsong+"-lyrics"
    print(songurl)
    start_urls = [songurl]

    def parse(self, response):
        self.logger.info('\n------hello, just here to get some lyrics')
        songlist = getsonglist()
        # songlist = songlist[1:]

        # item['lyric'] = " ".join(response.css("div.lyrics > p::text").extract()).strip()
        for songartist in songlist:
            artistsong = getsong(songartist)
            songurl = "https://genius.com/"+artistsong+"-lyrics"
            # yield response.follow(songurl, callback=self.parse_dir_contents)
            yield scrapy.Request(songurl, callback=self.parse_dir_contents)
        # return item
        # yield 'lyric': lyrics.css('')

    def parse_dir_contents(self, response):
        self.logger.info('Parse-dir-contents function called on {}'.format(response.url))
        lyrics = response.css("div.lyrics > p::text").getall()

        for i,lyrs in enumerate(lyrics):
            lyrics[i] = lyrics[i].strip()
            # lyrics[i] = re.sub(r'\[.*?\]\ *','',lyrics[i])
        lyrics = [lyr for lyr in lyrics if lyr]

        full_lyrics = ' '.join(lyrics)

        # lyr = ItemLoader(item=SongItem(), selector = full_lyrics)

        item = SongsItem()
        item['title'] = response.css("div.header_with_cover_art-primary_info > h1::text").extract()[0].strip()
        item['artist'] = response.css("div.header_with_cover_art-primary_info > h2 > a::text").extract()[0].strip()
        item['lyric'] = full_lyrics

        yield item
