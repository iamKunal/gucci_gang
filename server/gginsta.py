from json import loads

from requests import get

from datetime import datetime
from calendar import timegm
 
QUERY_ID = 17888483320059182
FIRST = 5
PAGE_LIST = 'witty_feed'
INSTA_URL = ['https://www.instagram.com/p/', '/']

CURRENT_TIME = None


class GGInsta:
    page = None
    seconds = None
    no_of_posts = None

    def __init__(self, page, seconds, no_of_posts):
        self.page = page
        self.seconds = seconds
        self.no_of_posts = no_of_posts
        global CURRENT_TIME
        CURRENT_TIME = timegm(datetime.utcnow().utctimetuple())

    def get_dict(self):
        if self.page is None:
            return []
        params = (
            ('__a', '1'),
        )
        response = get('https://www.instagram.com/' + self.page + '/', params=params)
        try:
            id = loads(response.text)['user']['id']
        except ValueError:
            return None
        params = (
            ('query_id', QUERY_ID),
            ('variables', '{"id":"' + str(id) + '","first":' + str(self.no_of_posts) + '}'),
        )

        response = get('https://www.instagram.com/graphql/query/', params=params)

        full_data = loads(response.text)
        if full_data["status"] == "ok":
            posts = full_data['data']['user']['edge_owner_to_timeline_media']['edges']
            return posts
        else:
            return None

    def generate_list(self):
        posts = self.get_dict()
        if posts is None:
            return None
        final_data = {'post': [],
                      'photo': [],
                      'video': []}
        for post in posts:
            temp_data = {}
            p = post['node']
            if CURRENT_TIME - p['taken_at_timestamp'] > self.seconds:
                continue

            if p['is_video']:
                temp_data['type'] = 'video'
            else:
                temp_data['type'] = 'photo'
            temp_data['channel'] = 'insta'
            temp_data['url'] = INSTA_URL[0] + p['shortcode'] + INSTA_URL[1]
            # print temp_data['url']
            temp_data['id'] = int(p['id'], 10)
            if len(p['edge_media_to_caption']['edges']) != 0:
                temp_data['caption'] = p['edge_media_to_caption']['edges'][0]['node']['text']
            else:
                temp_data['caption'] = None
            # print temp_data['caption']
            temp_data['timestamp'] = p['taken_at_timestamp']
            temp_data['likes'] = p['edge_media_preview_like']['count']
            temp_data['attachment'] = p['thumbnail_src']
            temp_data['weight'] = 100
            temp_data['comments'] = p['edge_media_to_comment']['count']
            temp_data['rate']=float(temp_data['likes']+temp_data['comments'])/float(timegm(datetime.utcnow().utctimetuple())-temp_data['timestamp'])
            final_data[temp_data['type']].append(temp_data)
            # print temp_data
        return final_data


if __name__ == "__main__":
    o = GGInsta(page=PAGE_LIST, seconds=60 * 60 * 24 * 100, no_of_posts=100)
    print o.generate_list()
