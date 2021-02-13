**tl;dr** clone the repo and run `python3 2_train.py`

Find a [live version on repl.it](https://repl.it/@misterybodon/mlimg), pressing **Run** to play it.

Set of scripts to:
1. Download datasets automatically
2. Train the model
3. Make predictions

## 1. Get the data
To train ML/DL models we need data. If we don't have it already, there are a few ways to get it:
1. Using an API
2. Webscrapping
3. Other source: Kaggle, ImageNet, papers with links, etc.

**Method 1**
For the first method we normally need API-key. Twitter, Youtube, Spotify, WeatherAPI have free APIs. Picsum has too. One of the strategies here is to use Picsum-API NodeJS-driver to download a set of cat images. 

The file for this purpose is `JSfetch.js`. This script is only partially written, but the strategy is fine.

**Method 2**
Using Python webscraping libraries. We use Beautiful Soup 4 or BS4. 

Large webpages load images dynamically using JS, hence a simple http request won't work (only X images are on the DOM at start). One alternative to BS4 is Selenium (see [StackOverflow](https://stackoverflow.com/questions/17436014/selenium-versus-beautifulsoup-for-web-scraping?rq=1)). But looking which JS was running we found the API call. With that and BS4 was enough to get 100+ cat photos.

Picsum images are transformed by the server according to query parameters. IMGIX API is used under the hood by Picsum. (just informative.)

Code is under `0_fetch.py`

## 2. Prepare data for ML
This step requires creating hfd5 files (h5) storing images in binary format. It's handy because features, labels and classes are all stored and loaded-from the binary file.

The next script to execute is `1_imgToH5.py`. This uses CV2 python image library, and writes features (images) and labels to a h5 file.

## 3. ML model
Code for training was blindly copied from the Andrew Ng course. The script is `2_train.py`.
