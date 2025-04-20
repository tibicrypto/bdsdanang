# scraping/spiders/danang/batdongsan.py
import scrapy
from scrapy_selenium import SeleniumRequest

class BatdongsanDanangSpider(scrapy.Spider):
    name = 'batdongsan_danang'
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'SELENIUM_DRIVER_NAME': 'chrome',
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_selenium.SeleniumMiddleware': 800
        }
    }

    def start_requests(self):
        districts = ['hai-chau', 'son-tra', 'ngu-hanh-son']
        for district in districts:
            yield SeleniumRequest(
                url=f"https://batdongsan.com.vn/da-nang/{district}",
                callback=self.parse,
                wait_time=10
            )

    def parse(self, response):
        for item in response.css('.re__card'):
            yield {
                'title': item.css('.title::text').get(),
                'price': self.clean_price(item.css('.price::text').get()),
                'location': self.clean_location(item.css('.location::text').get()),
                'district': response.url.split('/')[-1]
            }
    
    def clean_price(self, text):
        # Xử lý giá theo định dạng Đà Nẵng
        if 'thỏa thuận' in text.lower():
            return None
        return float(text.replace(' tỷ', '').strip())
