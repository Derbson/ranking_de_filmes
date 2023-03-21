import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://m.imdb.com/chart/moviemeter/?ref_=tt_ov_pop"]

    def parse(self, response):
        for filmes in response.css('.media-vertical-align'):
            yield{
                'position': filmes.css('.meter::text').get(),
                'titulos': filmes.css('.media-vertical-align h4::text').get(),
                'ano_lancamento': filmes.css('.media-vertical-align h4 .unbold::text').get()
            }
            


# filmes
# .media-vertical-align

# titulo
# .media-vertical-align h4

# ano de lançamento
# .media-vertical-align h4 .unbold

# position
# .meter




