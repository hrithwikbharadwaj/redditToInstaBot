# Reddit Instagram Meme Bot

## What is it ?

Reddit instagram bot, is a bot that uses web scrapping technologies to scarpe the most famous memes from reddit (Where memes are made) and post them to [@thiru.bot](https://www.instagram.com/thiru.bot/ "@thiru.bot") on instagram
It uses the following tags to find great memes
```
    ['dankmemes','ProgrammerHumor','memes','wholesomememes','comedyheaven']
```


## How does it work ?
The bot uses reddits api to log into reddit

Then the bot loops a 100 times and random choices one of the above tag to find an meme that makes sense as in is the hottest 🔥, then the bot checks if it's a textual meme or not, if it is it gets skipped else the image download and processing starts

The bot gets the post and waits for it to completely be loaded then it extracts the image url and checks if it a random image link or one from [imgur.com](https://imgur.com) if it's a random link the image is got and processed as in cropped for instagram, image id added to POSTED_CACHE and such stuff. Else if the image is from [imgur.com](https://imgur.com), the bot uses bs4 to scrape their website and get the image followed by the similar processing.

Finally credits to the aythors is added followed by creating an instagram post object and then finally posting it on instagram





### This readme was written by [iresharma](https://iresharma.me) as an entry to [Hacktoberfest](https://hacktoberfest.digitalocean.com)