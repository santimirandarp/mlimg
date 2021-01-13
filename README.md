**tl;dr** clone the repo and run `python3 2_train.py`

# Binary Classifier

As an excuse to learn ML we created this simple document describing a few ideas and basic steps.

The aim is to build a set of scripts to:
1. Download datasets automatically
2. Train the model
3. Make predictions


## 1. Get the data
To train ML models we need data. If we don't have it already, there are a few ways to get it:
1. Using an API
2. Webscrapping

**Method 1**
For the first method we normally need API-key. Twitter, Youtube, Spotify, WeatherAPI have free APIs. Picsum has too.

One of the strategies here is to use Picsum-API NodeJS-driver to download a set of cat images.

The file for this purpose is `JSfetch.js`.

This script is partially written. But the strategy looks promising.

**Method 2**
Another method is using Python webscraping libraries. We use Beautiful Soup 4 or BS4. 

Large webpages load images dynamically using JS, hence a simple http request won't work (only X images are on the DOM at start).

One alternative to BS4 is Selenium (see [StackOverflow](https://stackoverflow.com/questions/17436014/selenium-versus-beautifulsoup-for-web-scraping?rq=1)). But looking which JS was running we found the API call. With that and BS4 was enough to get 100+ cat photos.

Picsum images are transformed by the server according to query parameters. IMGIX API is used under the hood by Picsum. This has been taken into account.

The code is under `0_fetch.py`

## 2. Prepare data for ML
This step requires creating hfd5 files (h5) from the images. So we can have the features, labels and classes all loaded into the binary file.

There are many ways to deal with images in python, a small introduction is under `morescripts/images_start.py`. This is not part of the procedure, but it's worth to take a look.

The next script to execute is `1_imgToH5.py`. This uses CV2 python image library, and writes features (images) and labels to a h5 file.

## 3. ML model
This was almost blindly copied from the ML course. The script is `2_
train.py`.
