# Twiter Scraper
This script was written to pull tweets of one or more topics from Twitter, where a topic is anything that can by typed in the search bar.

### Dependencies
1. install Python (2 or 3)
2. pip install twarc

Before using twarc you will need to register an application at [apps.twitter.com](apps.twitter.com). Once you've created your application, note down the consumer key, consumer secret and then click to generate an access token and access token secret. With these four variables in hand you are ready to start using twarc.

### Useage
1. You will need to open the twitterScraper.py file
2. You will need to add the consumer key, consumer secret, access token, and access token secret and paste them into the file between single qoutes. 
3. You will need to add the language of the tweets, currently set at English.  
    * en: ENGLISH
    * es: Spanish
    * de: German
    * ja: Japanese
    * Others: https://developer.twitter.com/en/docs/developer-utilities/supported-languages/api-reference/get-help-languages.html
4. Update the list of topics you want to search for, topic_list.

I will say that twitter only allows 180 tweets to be pulled every 15 minutes, so huge topics will take some time so you might want to limit the number of topics to about 2 or so just incase the time is taking too long but you will just have to let the computer do it's work until its done!

Since you filled in yourself the keys, language, and topics running the file will be easy. Just run the command:

`python twitterScraper.py`  

### Contributors 
This file was created by [Caleb Crumley](https://github.com/crumleyc), in the Digital Humanities Lab at UGA. 

### Licensing 
Look at the [License](../../LICENSE)

### Future additions:
* This list is also a future addition.
