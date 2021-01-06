# Cat Image Detector

As an excuse to learn ML we created this simple document describing a few ideas and basic steps.

## 1. Get the data
To train ML models we need data. If we don't have it already, there are a few ways to get it:
1. Using an API
2. Webscrapping

**Method 1**
The first method normally needs us having an API-key. Twitter, Youtube, Spotify, WeatherAPI have free APIs. Picsum has too.

One of the strategies here is to use Picsum-API NodeJS-driver to download a set of cat images.

The file for this purpose is `JSfetch.js`.

**Method 2**
Another method is using Python webscraping libraries. We use Beautiful Soup 4 or BS4. 

The content of the images-page is being dynamically loaded using JS, hence a simple http request didn't work (only 9 images are on the DOM on start).

One option is Selenium as recommended on [StackOverflow](https://stackoverflow.com/questions/17436014/selenium-versus-beautifulsoup-for-web-scraping?rq=1). But looking which JS was running we found the API call. With that and BS4 was enough to get 100+ cat photos.

We had to research on IMGIX because the images are transformed by the server according to query parameters. IMGIX is an API used under the hood by Picsum. The code is under `Pyfetch-json.py`

Another path is to use **1.**. Part of the script is already written. Exactly the same functions in Python, written in JS should do.

## 2. Prepare data for ML

