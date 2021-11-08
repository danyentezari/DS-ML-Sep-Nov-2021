# Import the scrapy library
import scrapy
# Import a special class called CrawlerProcess from the folder scrapy.crawler
from scrapy.crawler import CrawlerProcess
# Import openpyxl for reading and writing Excel documents
from openpyxl import Workbook

# Instantiate a new workbook
wb = Workbook()

# Choose the active worksheet in the workbook
ws = wb.active

class PropertyListingSpider(scrapy.Spider):

    name = "propertylistingspider"
    start_urls = [
        "https://focused-poitras-08f701.netlify.app/",
    ]

    # Scrapy will pass the argument for "webPage"
    # after it runs the spider
    def parse(self, webPage):

        # Using CSS to find the card
        # theCards will a List containing HTML elements
        theCards = webPage.css('div.card')

        # Using Xpath to find the card
        # theCards = webPage.selector.xpath('/html/body/div[1]/div/div/div[1]/div/h5[2]/text()').get()
        
        # Loop through all of the cards
        for card in theCards:

            # Create an empty list to populate later
            excelRow = []

            # (1) Get the 'name' of the property
            # .css() method will retrieve the HTML element
            # .get() method will convert the HTML element to Python string
            name = card.css('h5:nth-child(2) ::text').get()
            # Add the name to the row 
            excelRow.append(name)

            # (2) Get the 'price' of the property
            price = card.css('h5.card-title ::text').get()
            # Add the price to the row
            excelRow.append(price)

            # (3) Get the 'first description' of the property
            firstDesc = card.css('p.card-description1 ::text').get()
            # Add the first desc to the row
            excelRow.append(firstDesc)

            # (4) Get the 'second description' of the property
            secondDesc = card.css('p.card-description2 ::text').get()
            # Add the second desc to the row
            excelRow.append(secondDesc)

            # (5) Get the 'url' of the picture of the property
            imgURL = card.css('img ::attr(src)').get()
            # Add the image url to the row
            excelRow.append(imgURL)

            # Add the excelRow to the worksheet
            ws.append(excelRow)

            print(excelRow)
    
        # Save the whole workbook       
        wb.save('simplelisting.xlsx')



# Instantiate and run our PropertyListingSpider
process = CrawlerProcess()
process.crawl(PropertyListingSpider)
process.start()