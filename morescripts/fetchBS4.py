from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

url = "https://unsplash.com/s/photos/cat"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
URLs = soup.find_all("img", class_="_2UpQX")


def download_image(image, index):
    response = requests.get(image, stream=True)
    imageString = image.split("/photo")[-1]
    imageName = imageString.split("?")[0].strip("-,.?*")
    file = open("./images/{}-{}.jpg".format(imageName, index), 'wb')
    
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response

for image in range(len(URLs)):
    download_image(URLs[image]["src"], image)

