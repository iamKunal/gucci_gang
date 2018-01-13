from bottle import run,route,template,request
import ggtwitter , gginsta , ggfb	
for _ in range(3):
	embed=[]
	
	fb_dict = ggfb.GGFB(url='wittyfeed',seconds=60*60*24*5, no_of_posts=10)
	fb_dict=fb_dict.fun_all().copy()
	#insta_dict = gginsta.GGInsta(page=link,seconds=60*60*24*5, no_of_posts=10)
	#insta_dict = insta_dict.generate_list()
	#twitter_dict = ggtwitter	.GGTwitter(page=link,seconds=60*60*24*5, no_of_posts=10)
	#twitter_dict = twitter_dict.final_data
	post_total = fb_dict['post']#+insta_dict['post']+twitter_dict['post']
	#print len(fb_dict['post'])
	# photo_total = fb_dict['photo']+insta_dict['photo']+twitter_dict['photo']
	# video_total = fb_dict['video']+insta_dict['video']+twitter_dict['video']
	post_total = sorted(post_total, key=lambda k: k['timestamp'], reverse=True)
	
	for post in post_total:
		if post['channel']=='facebook':
			embed.append(post['embed'])
