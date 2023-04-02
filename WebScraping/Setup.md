pip install Scrapy

scrapy startproject ietf_scraper

Others:
scrapy genspider ietf pythonscraping.com
scrapy runspider ietf.py

scrapy runspider wikipedia.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10