from classify_fb import *
import os
import subprocess
import multiprocessing

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
    return output


if __name__ == '__main__':
    fb_class = GGFB('WittyFeed', 60 * 60 * 24 * 30, 25)
    final_data = fb_class.fun_all()

    p = multiprocessing.Pool(len(final_data['post']), init_workers)
    print(p.map(f, final_data['post']))

    # b = os.popen('python classify_fb.py '+'https://ia.wittyfeed.com/story/61173/real-faces-behind-the-famous-memes?utm_source=IA&utm_medium=SOCIAL&utm_campaign=38571-campaign&utm_hash=onGGb&i=2')
    # print b
