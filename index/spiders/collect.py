import scrapy
from index.utils.errors import SeridNotIsNumberError,SeridNotInformedError
from index.utils.urls import Urls


class CollectSpider(scrapy.Spider):
    name = 'collect'
    allowed_domains = [Urls['ipeadata_accept'].value]

    def start_requests(self):
        """Start

        :required:
            :serid: number
        
        :raise:
            ValueError

        """

        serid: str = getattr(self, 'serid', None)#capture key serid
        if not serid:
            raise SeridNotInformedError()
        if not serid.isnumeric():
            raise SeridNotIsNumberError()

        yield scrapy.Request(url=f'{Urls["ipeadata_request"].value}{serid}', callback=self.parse)

    def parse(self, response):
        for row in response.css('table#grd_DXMainTable'):
            for celula in row.css('tr')[3:]:
                year_month, index = celula.css('td')
                year_month = year_month.css('::text').get()
                index = index.css('::text').get()
                yield {'date': year_month, 'index': index}
