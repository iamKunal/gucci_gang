from classify_fb import *
import os
import subprocess
import multiprocessing
from collections import Counter
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64
def init_workers():
    pass

def f(x):
    process = subprocess.Popen(["python", "classify_fb.py",
                                x['attachment']],
                               stdout=subprocess.PIPE)
    output, error = process.communicate()
    print error
    try:
        process.kill()
    except OSError:
        pass
    return output.strip().split('\n')


def get_tags(final_data):
#    fb_class = GGFB('WittyFeed', 60 * 60 * 24 * 30, 15)
#    final_data = fb_class.fun_all()

    p = multiprocessing.Pool(len(final_data['post']), init_workers)
    topics = p.map(f, final_data['post'])
    topics = [item.strip() for sublist in topics for item in sublist]
    topics = filter(lambda x: x!='', topics)
    print topics
    return get_world_cloud(topics)
def get_world_cloud(topics):
    wordcloud = WordCloud(width=1920, height=1080, background_color="white").generate('\n'.join(topics))
    img = wordcloud.to_image()
    path = '/tmp/' + str(timegm(datetime.utcnow().utctimetuple())) + '.png'
    img.save(path)
    return path

print get_tags(GGFB('WittyFeed', 60 * 60 * 24 * 30, 15).fun_all())

