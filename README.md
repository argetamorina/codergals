# Scraping FX exchange rates from the Reuters website

### Installation
We need the Scrapy library along with PyMongo for storing the data in MongoDB.

To install Scrapy with pip (with your virtualenv activated) type:
* $ pip install Scrapy

To install PyMongo with pip type:
* $ pip install pymongo

### Scrapy project

To start a new Scrapy project, you must type in command line
* $ scrapy startproject name_of_project

### Running the project

To get up running the project you must run the command within the “stack” directory:
* $scrapy crawl stack

To store the extracted data in json format we type :
* $scrapy crawl stack -o items.json -t json

To get the data for every 60 seconds we type the following command on terminal:
* watch -n 60 scrapy crawl stack
