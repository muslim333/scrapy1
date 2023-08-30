import scrapy
from monitors import MyCustomMonitor
from ..items import CovidItem

class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']
    
    custom_settings = {
        'SPIDERMON_ENABLED': True,
        'SPIDERMON_SPIDER_CLOSE_MONITORS': (
            MyCustomMonitor,
        )
    }

    def parse(self, response):
        rows = response.xpath('//table[@id="main_table_countries_today"]/tbody/tr')
        
        for row in rows:
            country = row.xpath(".//td[2]/a/text() | .//td[2]/span/text()").get()
            total_case = row.xpath(".//td[3]/text()").get()
            total_deaths = row.xpath(".//td[5]/text()").get()
            total_recovered = row.xpath(".//td[7]/text()").get()
            active_cases = row.xpath(".//td[9]/text()").get()
            critical_cases = row.xpath(".//td[10]/text()").get()

            item = CovidItem(
                CountryName=country,
                TotalCase=total_case,
                TotalDeaths=total_deaths,
                TotalRecovered=total_recovered,
                ActiveCases=active_cases,
                CriticalCases=critical_cases
            )
            yield item
