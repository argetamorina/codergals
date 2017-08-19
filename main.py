import urllib.request
import re


urls = ["https://www.reuters.com/"]
i = 0

# regex = "<title>(.+?)</title>"
# pattern = re.compile(regex)


while i < len(urls):
    htmlfile = urllib.request.urlopen(urls[i])
    htmltext = htmlfile.read()
    title = re.findall('<title>(.*)</title>', htmltext.decode('utf-8'))


    print (title)
    i+=1
