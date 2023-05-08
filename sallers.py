import scrapy
from bs4 import BeautifulSoup

# no 'start_urls' no final estamos dizendo todas as páginas que o site tem e que vamos percorrer, vamos usar esse 'start_urls' lá no final 'prox_pag'
class SallersSpider(scrapy.Spider):
    name = 'sallers'
    allowed_domains = ['ilab.org']  
    start_urls = ['https://ilab.org/page/affiliate-search-results?business&bookseller&country&city&specialty&association&submit&page=1']

# usar o BeautifulSoup foi necessário para remover caracteres extras, por isso fazemos o parsing do HTML
    def clear_address(self, address):
        soup = BeautifulSoup(address, 'html.parser')
        return soup.get_text().strip().replace('\t', '').replace('\n', ' ')
# aqui estmamos usando o '.item' que tem todas as informações que precisamos e estamos selecionando cada uma logo abaixo.
    def parse(self, response):
        for sallers in response.css('.item'):
            yield {
                'business': sallers.css('.business ::text').get(),
                'name': sallers.css('.name ::text').get(),
                'phone': sallers.css('.phone a::text').get(),
                'site': sallers.css('.website a::text').get(),
                'email': sallers.css('.email a::text').get(),
                'address': self.clear_address(sallers.css('.address').get())
            }

        prox_pag= response.xpath('//*[@id="primary"]/section/div[1]/div[2]/a').attrib['href']
        if prox_pag is not None:
            yield response.follow(prox_pag, callback=self.parse)