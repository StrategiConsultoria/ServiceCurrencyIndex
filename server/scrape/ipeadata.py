from datetime import date as dt

from requests_html import HTMLSession


class IpeadataScrape():
    def __init__(self,serid):
        self.url_font = f'http://www.ipeadata.gov.br/exibeserie.aspx?serid={serid}'
    def start(self):
        session = HTMLSession()
        return self.scraper(session.get(self.url_font))

    def scraper(self,response):
        table = response.html.find('table#grd_DXMainTable',first=True)
        for row in table.find('tr')[3:]:
            try:
                date, index = row.find('td')

                date = self.string_to_data_string(date.text)
                index = self.replace_dot_index(index.text)
                
                yield {'date':date,'index':index}
            except:
                ...
    def string_to_data_string(self,date):
        year, month = date.split('.')
        return f'1-{month}-{year}'

    def replace_dot_index(self,index:str):
        return index.replace(',','.')
        


        
