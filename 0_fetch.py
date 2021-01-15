from bs4 import BeautifulSoup # webscraping library

import requests
import urllib.request
import shutil

def queryForImages(queryWord, imagesNum=5, pages=1):
    """
    collects imagesNum*pages images. (only way possible).

    queryWord: example "cat". String
    imagesNum: number of images. Number.
    pages: number of pages. Number.

    array of images' urls 
    """
    baseUrl="https://unsplash.com"
    route = "/napi/search/photos"
    #there is limit 30 imgs/page, so we need a loop
    links = []
    for page in range(pages):
        query = "?query={}&per_page={}&page={}&xp=feedback-loop-v2:control".format(queryWord, imagesNum, page)
        url = baseUrl+route+query 
        print("requesting:", " ", url)
        response = requests.get(url).json() 
        # server responds w/ JSON data
        results = response["results"] # access object
        for index in range(len(results)):
           links.append(results[index]["urls"]["raw"])
    return links

def download_images(links, outdir, IMGIX="&h=200&w=200&fit=clamp"):
    """
    links: array of images links
    outdir: dir where to save images
    IMGIX: image-processing query string.
    """
    for link in range(len(links)):
        url = links[link]+IMGIX
        # set up
        cleanUrl = url.split("/photo")[-1]
        imageName = cleanUrl.split("?")[0].strip("-,.?*")
        file = open("{}/{}-{}.jpg".format(outdir, imageName,link), 'wb') # below write binary data "wb" (jpg) to file.

        response = requests.get(url, stream=True)
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, file)
        del response
     return 1

download_images( queryForImages("elephant", 100, 5), 
                "./images/raw/elephants")
