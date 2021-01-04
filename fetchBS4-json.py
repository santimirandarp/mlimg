from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

# found the "GET" request to the API

def queryForImages(queryWord, imagesNum=30, pages=5):
    """
    collects imagesNum*pages images. (no other way possible).

    queryWord: example "cat", a string
    imagesNum: number of images, a number.
    pages: number of pages, a number.

    returns urls of images
    """
    baseUrl="https://unsplash.com"
    route = "/napi/search/photos"
    #there is limit 30 imgs/page, so we need a loop
    links = []
    for page in range(pages):
        query = "?query={}&per_page={}&page={}&xp=feedback-loop-v2:control".format(queryWord, imagesNum, page)
        url = baseUrl+route+query 
        print("page", page)
        print("url", url)
        response = requests.get(url).json() 
        # server responds to an API call with JSON data
        results = response["results"] # access json data
        for index in range(len(results)):
           links.append(results[index]["urls"]["thumb"])
    return links

def download_images(links):
    "links: array of images links"
    for link in range(len(links)):
        url = links[link]
        response = requests.get(url, stream=True)
        cleanUrl = url.split("/photo")[-1]
        imageName = cleanUrl.split("?")[0].strip("-,.?*")
        file = open("./images/{}-{}.jpg".format(imageName,link), 'wb')
        
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, file)
        del response

download_images(queryForImages("cat", 100))
