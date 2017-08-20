FX scraping values from public websites 
<!--Execute the scrapy project  -->
scrapy crawl stack
<!--Write the data taken from the website to a json format -->
scrapy crawl stack -o items.json -t json
<!-- Get the data after every specific time-->
watch -n 60 scrapy crawl stack
