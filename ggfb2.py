from facepy import GraphAPI
import time
from datetime import datetime
from calendar import timegm
import requests
import json

posts = []
images = []
videos = []
fb = {}

TMP_TOKEN = 'EAACEdEose0cBAJaZBbKUvWvNCBmb8iEEgv9F9LyAJFaZCHLaS9xFLbjuAyP5vOQgE8zRTJHhLbnnfZAaZCzCxi1Sf2mpKqst5onwxAZAuDXnJxZAXFXRGHLZBu6JnBasoJnEQaCEbwuIGefvIQp2jcxgPp8ZCIxq6IDPVzdQmg7HwZABjkR6qg3EsWw5rNfg6E2j1VVZBFsiPytQZDZD'
PER_TOKEN = 'EAACEdEose0cBAJaZBbKUvWvNCBmb8iEEgv9F9LyAJFaZCHLaS9xFLbjuAyP5vOQgE8zRTJHhLbnnfZAaZCzCxi1Sf2mpKqst5onwxAZAuDXnJxZAXFXRGHLZBu6JnBasoJnEQaCEbwuIGefvIQp2jcxgPp8ZCIxq6IDPVzdQmg7HwZABjkR6qg3EsWw5rNfg6E2j1VVZBFsiPytQZDZD'


class ggfb():
    url = None
    seconds = None
    no_of_posts = None
    time_gap = None
    graph = GraphAPI(oauth_token=TMP_TOKEN, version='2.10')

    def fun_feeds(self):
        json = self.graph.get(self.url + '/feed?limit=' + str(self.no_of_posts) + '&since=' + str(self.time_gap) +"&fields=created_time,reactions.limit(0).summary(total_count),comments.limit(0).summary(total_count),message")["data"]
        for feed in json:
            post = {}
            post['reactions'] = int(feed["reactions"]["summary"]["total_count"])
            post['comments'] = int( feed["comments"]["summary"]["total_count"])
            post['timestamp'] = timegm(time.strptime(feed['created_time'], '%Y-%m-%dT%H:%M:%S+0000'))
            post['caption'] = feed.get('message')
            post['id'] = feed['id']
            post['attachment'] = 'None'
            post['weight'] = 'None'
            post['type']="post"
            post['url'] = 'www.facebook.com' + str(feed['id'])
            post['embed'] = 'https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2F' + self.url + '%2Fposts%2F' + str(feed['id'].split('_')[1])
            posts.append(post.copy())
    def fun_images(self):
        json = self.graph.get(self.url + '/photos?limit=' + str(self.no_of_posts) + '&since=' + str(self.time_gap) +"&fields=created_time,reactions.limit(0).summary(total_count),comments.limit(0).summary(total_count),message")["data"]
        for photo in json:
            image = {}
            image['reactions'] = int(photo['reactions']['summary']['total_count'])
            image['comments'] = int(photo['comments']['summary']['total_count'])
            image['timestamp'] = timegm(time.strptime(photo['created_time'], '%Y-%m-%dT%H:%M:%S+0000'))
            image['id'] = photo['id']
            image['attachment'] = 'None'
            image['weight'] = 'None'
            image['type']='photo'
            image['url'] = 'www.facebook.com' + str(photo['id'])
            images.append(image)

    def fun_videos(self):
        json = self.graph.get(self.url + '/videos?limit=' + str(self.no_of_posts) + '&since=' + str(self.time_gap) +"&fields=created_time,reactions.limit(0).summary(total_count),comments.limit(0).summary(total_count),description")["data"]
        for vid in json:
            video = {}
            video['reactions'] = int(vid['reactions']['summary']['total_count'])
            video['comments'] = int(vid['comments']['summary']['total_count'])
            video['timestamp'] = timegm(time.strptime(vid['created_time'], '%Y-%m-%dT%H:%M:%S+0000'))
            video['caption'] = vid.get('description')  ##very less captions
            video['id'] = vid['id']
            video['attachment'] = 'None'
            video['weight'] = 'None'
            video['type']='video'
            video['url'] = 'www.facebook.com' + str(vid['id'])
            video['embed'] = 'https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2F' + self.url + '%2Fvideos%2F' + str(vid['id']) + '%2F'
            videos.append(video)

    def __init__(self, url, seconds, no_of_posts):
        self.url = url
        self.seconds = seconds
        self.no_of_posts = no_of_posts
        self.time_gap = timegm(datetime.utcnow().utctimetuple()) - self.seconds
    def fun_all(self):
        self.fun_feeds()
        self.fun_images()
        self.fun_videos()
        final_data = {'post': posts,
             'photo': images,
             'video': videos}
        return final_data

if __name__ == '__main__':
    fb_class = ggfb('wittyfeed', 60*60*24*30, 25)
    print(fb_class.fun_all())   ##this is to be finally returned
