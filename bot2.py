
import urllib.request
import time
import keyboard
from PIL import Image
import math
from glob import glob
import random
import praw,re,requests,pprint,importlib,os, time, datetime, urllib.request,string, sys
from bs4 import BeautifulSoup
from PIL import Image
from instabot import Bot
bot=Bot()


bot.login(username="Thiru.bot",password="THarunarayana135")

post_ids=[]

reddit = praw.Reddit(client_id='l8FxsJZiRaabPw',
        client_secret='wldsk-Z0Q9hy_LbNGdU6GG2UdDw',
        username='thiru69420',
        password='Pmachi@2007',
        user_agent='chrome')


def DLimage(url, filePath, fileName):
        fullPath = filePath + fileName + '.jpg'
        urllib.request.urlretrieve(url, fullPath)

def IsImageLink(url):  #checks if url is image, returns image type (png,jpg, jpeg)
    LinkRegex=re.compile('((https:|http:)?\/\/.*\.(png|jpg|jpeg))')
    results=LinkRegex.findall(url)
    if results:
        return results[0][2]
    else:
        return False



filePath = "images"
list1=['saimansays','memes','wholesomememes','comedyheaven','bakchodi']



captionTags = "#meme #memebot #dankmemes #followThiru.jpg"


captionText = "haha Lol"

waitTime = 2

numRounds = 100

postFrequency = 500
POSTED_CACHE = 'posted_posts.txt'
numPics = 5
def already_tweeted(post_id):
    ''' Checks if the reddit Twitter bot has already tweeted a post. '''
    found = False
    with open(POSTED_CACHE, 'r') as in_file:
        for line in in_file:
            if post_id in line:
                found = True
                break
    return found

def log_insta(post_ids):
    for post_id in post_ids:
        with open(POSTED_CACHE, 'a') as out_file:
            out_file.write(str(post_id) + '\n')
def CropToInstagram(filename):
    img=Image.open(filename)
    x,y=img.size
    width, height = img.size
    img = img.resize((1000, 1020), Image.NEAREST) #image resize. width/height

    try:

        new_name=filename[:-3]+'jpg'
        img=img.convert('RGB')
        os.unlink(filename)
        img.save(new_name)
        filename=new_name
    except Exception as e:
        print(e)


    return filename
counter=0
for x in range(numRounds):
        red=random.choice(list1)
        print(red)
        subreddit = reddit.subreddit(red)
        new_memes = subreddit.hot(limit=numPics)
        authors = []

        photoAlbum = []
        print("Round/post number:", x)
        for submission in new_memes:
                if submission.is_self == True:
                        print("Post was text, skipping to next post.")
                        continue
                else:
                        pass
                url = submission.url
                time.sleep(waitTime)
                fileName = str(submission)


                time.sleep(waitTime)

                # try:
                #         DLimage(url, filePath, fileName)
                # except:
                #         print("scratch that, next post.")
                #         continue
                if IsImageLink(url) and not already_tweeted(submission.id):
                    try:
                        img=requests.get(submission.url)
                        filename=str(counter)+'.'+IsImageLink(submission.url)
                        print(filename)
                        filename=os.path.join('images', filename)
                        print(filename)

                        imagefile=open(filename, 'wb')
                        imagefile.write(img.content)
                        imagefile.close()
                        post_ids.append(submission.id)
                        log_insta(post_ids)

                        filename=CropToInstagram(filename)
                        photoAlbum.append({'File':filename, 'Title':submission.title}) #dictionary format

                        counter+=1
                    except Exception as e:
                        print(e)

                elif str(submission.url).lower().startswith('https://imgur.com') or str(submission.url).lower().startswith('http://imgur.com') and counter<max_images:
                    try:
                        html_page = urllib.request.urlopen(submission.url)
                        soup = BeautifulSoup(html_page, 'lxml')
                        images = []
                        for img in soup.findAll('img'):
                            images.append('https:'+img.get('src'))

                        img=requests.get(images[0])
                        filename=str(counter)+'.'+images[0][-3:]
                        filename=os.path.join('images', filename)
                        imagefile=open(filename, 'wb')
                        imagefile.write(img.content)
                        imagefile.close()

                        filename=CropToInstagram(filename)


                        photoAlbum.append({'File':filename, 'Title':submission.title}) #dictionary format

                        counter+=1
                    except Exception as e:
                        print(e)



        authors = ''.join(str(e + ', ') for e in authors)
        print(photoAlbum)
        for photo in photoAlbum:

                print(photo['File'])
                raju=photo['File']
                captionText=photo['Title']
                bot.upload_photo(raju,caption=(captionText + '\n' + 'Pulled from '+ 'r/'+red + ' '+ 'Reddit Authors:' + ' ' + authors[0:(len(authors)-2)] + '.' + '.' + '.'  +  '\n' + captionTags))
        # for filename in glob(filePath + '/*'):
        #     os.remove(filename)
        print("Sleeping")
        time.sleep(50)
