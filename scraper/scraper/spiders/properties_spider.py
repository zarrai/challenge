from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from scraper.scraper.items import ScraperItem


class PropertiesSpider(CrawlSpider):
    name = "properties"
    allowed_domains = ["www.presidency.ucsb.edu"]
    start_urls = [
        "https://www.presidency.ucsb.edu/documents/app-categories/written-statements/presidential/statements-administration-policy?items_per_page=10&page=127"
    ]

    rules = (
        Rule(
            LinkExtractor(allow=(r"page=\d+")),
            callback="parse_property",
            follow=True,
        ),
    )

    def parse_property(self, response):
        property_loader = ItemLoader(item=ScraperItem(), response=response)
        property_loader.default_output_processor = TakeFirst()
        
        property_loader.add_xpath(
            "bill_number", "//div[@class='field-title']/p/a/text()"
        )
        property_loader.add_xpath(
            "bill", "//div[@class='field-title']/p/a/text()"
        )
        property_loader.add_css(
            "congress", "span.date-display-single::text"
        )
        property_loader.add_css(
            "date",
            "span.date-display-single::text",
        )
        property_loader.add_xpath(
            "link", "//div[@class='field-title']/p/a/@href"
        )
        

        yield property_loader.load_item()
