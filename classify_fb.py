from facepy import GraphAPI
import time
from datetime import datetime
from calendar import timegm
import requests
import json
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import time
import sys
posts = []
images = []
videos = []
fb = {}
id_list = []
TMP_TOKEN = 'EAACEdEose0cBACAOvrU9C0hZALmVacUDgvWQW94kzw2ZBv9wvGcWqFphtulwLvxtSLaMjjtYEo0ilO9DZBvJr0cjKAImfN9FCkegxLtHyfvRygydbEQkf1f6VaVE1Ag6ZBm4TlzCvwwBZCxCdqGU8q9BfpljGh2WCuZCb9MZAVFs3WZAT3ApYGiDZCRZBCyaOqqXkP8aH7PTM6IgZDZD'
PER_TOKEN = 'EAACEdEose0cBACvYlc3kFWuOMotBFZBlCKkCmFoPt2BxT2GSzKAp5pqd7ImD7pku75rBft4ZCD9qDmDjhoiA7MoTrbkYpdNhAiZBssOQUy2A3g8vLZAyaOhn4eoSZBTaF4tMPe6uc1UvFhbVMZAPKMjNnN2SEbtxEYJoUjQ0dBXGsOTPyRIx1MD0ynZC0x2gJVMzUIWdRafvx2ugraX6gzR'
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from HTMLParser import HTMLParser
from boilerpipe.extract import Extractor


def text_extractor(URL):
    extractor = Extractor(extractor='ArticleExtractor', url=URL).getText()
    return extractor


def classify(text):
    try:
        client = language.LanguageServiceClient()
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)
        response = client.classify_text(
            document=document
        )
        return response.categories
    except:
        return [None]


class GGFB():
    url = None
    seconds = None
    no_of_posts = None
    time_gap = None
    graph = GraphAPI(oauth_token=TMP_TOKEN, version='2.10')
    posts = []
    images = []
    videos = []
    fb = {}

    def fun_feeds(self):
        json = self.graph.get(self.url + '/feed?limit=' + str(self.no_of_posts) + '&since=' + str(
            self.time_gap) + "&fields=created_time,reactions.limit(0).summary(total_count),comments.limit(0).summary(total_count),message,link")[
            "data"]
        for feed in json:
            post = {}
            post['reactions'] = int(feed["reactions"]["summary"]["total_count"])
            post['comments'] = int(feed["comments"]["summary"]["total_count"])
            post['timestamp'] = timegm(time.strptime(feed['created_time'], '%Y-%m-%dT%H:%M:%S+0000'))
            post['caption'] = feed.get('message')
            post['id'] = feed['id']
            post['channel'] = "fb"
            post["attachment"] = feed.get("link")
            post['weight'] = 'None'
            post['type'] = "post"
            post['url'] = 'www.facebook.com' + str(feed['id'])
            post[
                'embed'] = 'https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2F' + self.url + '%2Fposts%2F' + str(
                feed['id'].split('_')[1])
            self.posts.append(post.copy())

    def fun_images(self):
        json = self.graph.get(self.url + '/photos?limit=' + str(self.no_of_posts) + '&since=' + str(
            self.time_gap) + "&fields=created_time,reactions.limit(0).summary(total_count),comments.limit(0).summary(total_count),message,link")[
            "data"]
        for photo in json:
            image = {}
            image['reactions'] = int(photo['reactions']['summary']['total_count'])
            image['comments'] = int(photo['comments']['summary']['total_count'])
            image['timestamp'] = timegm(time.strptime(photo['created_time'], '%Y-%m-%dT%H:%M:%S+0000'))
            image['id'] = photo['id']
            image['channel'] = "fb"
            image["attachment"] = photo.get('link')
            image['weight'] = 'None'
            image['type'] = 'photo'
            image['url'] = 'www.facebook.com' + str(photo['id'])
            self.images.append(image)

    def fun_videos(self):
        json = self.graph.get(self.url + '/videos?limit=' + str(self.no_of_posts) + '&since=' + str(
            self.time_gap) + "&fields=created_time,reactions.limit(0).summary(total_count),comments.limit(0).summary(total_count),description,link")[
            "data"]
        for vid in json:
            video = {}
            video['reactions'] = int(vid['reactions']['summary']['total_count'])
            video['comments'] = int(vid['comments']['summary']['total_count'])
            video['timestamp'] = timegm(time.strptime(vid['created_time'], '%Y-%m-%dT%H:%M:%S+0000'))
            video['caption'] = vid.get('description')  ##very less captions
            video['id'] = vid['id']
            video["attachment"] = vid.get('link')
            video['channel'] = "fb"
            video['weight'] = 'None'
            video['type'] = 'video'
            video['url'] = 'www.facebook.com' + str(vid['id'])
            video[
                'embed'] = 'https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2F' + self.url + '%2Fvideos%2F' + str(
                vid['id']) + '%2F'
            self.videos.append(video)

    def __init__(self, url, seconds, no_of_posts):
        self.posts = []
        self.images = []
        self.videos = []
        self.fb = {}
        self.url = url
        self.seconds = seconds
        self.no_of_posts = no_of_posts
        self.time_gap = timegm(datetime.utcnow().utctimetuple()) - self.seconds

    def fun_all(self):

        self.fun_feeds()
        self.fun_images()
        self.fun_videos()
        final_data = {'post': self.posts,
                      'photo': self.images,
                      'video': self.videos}
        return final_data

    def classify(self, text):
        try:
            client = language.LanguageServiceClient()
            document = types.Document(
                content=text,
                type=enums.Document.Type.PLAIN_TEXT)
            response = client.classify_text(
                document=document
            )
            return response.categories[0].name
        except:
            return None


def f(x):
    categories = classify(text_extractor(x["attachment"]))
    print x["attachment"], categories


if __name__ == '__main__':
    # start = 0
    # while True:
    #     fb_class = GGFB('WittyFeed', 60 * 60 * 24 * 30, 25)
    #     final_data = fb_class.fun_all()  ##this is to be finally returned
    #     for posts_class in final_data:
    #         # for post in final_data[posts_class]:
    #         # if bool(bool(post["id"] not in id_list) and bool(
    #         #         post["attachment"] and len(post["attachment"].strip()) > 0)):
    text = text_extractor(sys.argv[1])
    # print text
    categories = classify(text)
    # print sys.argv[1], categories
    for category in categories:
        if (category):
            print category.name.split('/')[-1]
