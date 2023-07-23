import scrapy
import numpy as np

class LakmeSpider(scrapy.Spider):
    name = 'lakme'
    start_urls = ['https://www.nykaa.com/brands/lakme/c/604?page_no=1&sort=popularity&intcmp=brand_menu,most_viewed,lakme&eq=desktop']
    page_number = 1
    
 
    
    def parse(self, response):
        product_links = response.xpath("//div[@class ='css-d5z3ro']/a[@class='css-qlopj4']/@href").getall()
            
            
        for link in product_links:
            yield response.follow(link, callback=self.parse_product_page)
    
    
            

    
    def parse_product_page(self, response):
        product_name = response.xpath("//h1[@class = 'css-1gc4x7i']/text()").get()
        colors = response.xpath("//select[@class = 'css-2t5nwu']/option/text()").getall()
        # sizes = response.css('.product-variations .size-variations a::text').getall()
        
        availabilities = "available"
      
        prices = response.xpath("//span[@class = 'css-1jczs19']/text()").get()
        
        yield{
            'Productname': product_name,
            'price': prices,
            'color': colors,
            'available or not': availabilities
            
        }
        
        self.page_number += 1
        if self.page_number <4:
            next_page = f'https://www.nykaa.com/brands/lakme/c/604?page_no={self.page_number}&sort=popularity&intcmp=brand_menu,most_viewed,lakme&eq=desktop'
            yield response.follow(next_page, callback=self.parse)   
    
