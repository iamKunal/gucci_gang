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

TMP_TOKEN = 'EAACEdEose0cBAPBf0o6HAQxap53UbwofDTu2K4eQp37tNIa8P8ZBQaaYW3fyTg3iMwk8GyrSan4sK5rO9ITcEbXSl17JEASL8h3u2FLbsvlnUner5PMKakKt4z4qEKTWgMdC8bcgeO6iLgZB9yMzCLBDB1GxNCqi1fqZBME444ZByqt3VYXZCpLkgQnXYj5gt0zH99LBBJegehlcUpEL9'
PER_TOKEN = 'EAAEapYGWuvYBAENWIYn6eBbecEYjOP2V8GvLEXw9ZBhw6ASzrl0MrWy4pFuAqjehiIV7PxIREozT10ZAQ5AMJWQnegIcDTBDQvbVkvisp83upZCVIqrAAixwW4vosZASbNibJGHBSp4p2HwDwKZAxCecGzLoxoJjh18Qr6atSQ3tzPKDXEphc'


class ggfb():
    url = None
    seconds = None
    no_of_posts = None
    time_gap = None
    graph = GraphAPI(oauth_token=TMP_TOKEN, version='2.10')

    def fun_feeds(self):
        time_gap = int(time.time()) - self.seconds
        json = self.graph.get(self.url + '/feed?limit=' + str(self.no_of_posts) + '&since=' + str(self.time_gap))['data']

        for feed in json:
            post = {}
            reaction = self.graph.get(feed['id'] + '?fields=reactions.limit(0).summary(total_count)')
            comments = self.graph.get(feed['id'] + '?fields=comments.limit(0).summary(total_count)')
            post['reactions'] = int(reaction['reactions']['summary']['total_count'])
            post['comments'] = int(comments['comments']['summary']['total_count'])
            post['timestamp'] = timegm(time.strptime(feed['created_time'], '%Y-%m-%dT%H:%M:%S+0000'))
            post['caption'] = feed.get('message')
            post['id'] = feed['id']
            post['attachment'] = 'None'
            post['weight'] = 'None'
            post['type']='type'
            post['url'] = 'www.facebook.com' + str(feed['id'])
            post['embed'] = 'https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2F' + self.url + '%2Fposts%2F' + str(feed['id'].split('_')[1])
            posts.append(post.copy())

    def fun_images(self):
        json = self.graph.get(self.url + '/photos?limit=' + str(self.no_of_posts) + '&since=' + str(self.time_gap))['data']
        for photo in json:
            image = {}
            reaction = self.graph.get(photo['id'] + '?fields=reactions.limit(0).summary(total_count)')
            comments = self.graph.get(photo['id'] + '?fields=comments.limit(0).summary(total_count)')
            image['reactions'] = int(reaction['reactions']['summary']['total_count'])
            image['comments'] = int(comments['comments']['summary']['total_count'])
            image['timestamp'] = timegm(time.strptime(photo['created_time'], '%Y-%m-%dT%H:%M:%S+0000'))
            image['caption'] = 'None'  ##very less captions
            image['id'] = photo['id']
            image['attachment'] = 'None'
            image['weight'] = 'None'
            image['type']='type'
            image['url'] = 'www.facebook.com' + str(photo['id'])
            images.append(image)

    def fun_videos(self):
        json = self.graph.get(self.url + '/videos?limit=' + str(self.no_of_posts) + '&since=' + str(self.time_gap))[
            'data']
        for vid in json:
            video = {}
            reaction = self.graph.get(vid['id'] + '?fields=reactions.limit(0).summary(total_count)')
            comments = self.graph.get(vid['id'] + '?fields=comments.limit(0).summary(total_count)')
            video['reactions'] = int(reaction['reactions']['summary']['total_count'])
            video['comments'] = int(comments['comments']['summary']['total_count'])
            video['timestamp'] = timegm(time.strptime(vid['updated_time'], '%Y-%m-%dT%H:%M:%S+0000'))
            video['caption'] = vid['description']  ##very less captions
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


# if __name__ == '__main__':
#     fb_class = ggfb('wittyfeed', 10000, 25)
#     fb_class.fun_feeds()
#     fb_class.fun_images()
#     fb_class.fun_videos()
#     fb = {'posts': posts, 'images': images, 'videos': videos}
#     print(fb)   ##this is to be finally returned
