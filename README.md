# Cat Image Detector

As an excuse to learn ML we created this simple document describing a few ideas and basic steps.

## 1. Get the data
To train ML models we need data. If we don't have it already, there are a few ways to get it:
1. Using an API
2. Webscrapping

**Method 1**
The first method normally needs us having an API-key, and we may or may not have to pay for that. Twitter, Youtube, Spotify, WeatherAPI have free APIs. Picsum has too.

One of the strategies here is to use Picsum API, NodeJS driver to download a set of cat images.

The file for this purpose is `fetch.js`.
**Method 2**
Another method is using some python webscraping library. Here we use Beautiful Soup 4 or BS4. The file for this purpose is `fetch.py`.

Because the content of the page is being dynamically loaded using javascript, a simple http request didn't fill the gaps (as only 9 images are on the DOM on start).

So we decided to try Selenium instead as recommended on [StackOverflow](https://stackoverflow.com/questions/17436014/selenium-versus-beautifulsoup-for-web-scraping?rq=1).

## 2. Prepare data for ML

