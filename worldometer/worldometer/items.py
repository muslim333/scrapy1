import scrapy

class CovidItem(scrapy.Item):
    CountryName = scrapy.Field()
    TotalCase = scrapy.Field()
    TotalDeaths = scrapy.Field()
    TotalRecovered = scrapy.Field()
    ActiveCases = scrapy.Field()
    CriticalCases = scrapy.Field()
