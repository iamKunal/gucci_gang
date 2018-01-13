from bottle import run,route,template,request,static_file
import ggtwitter , gginsta , ggfb





@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./static/js')


@route('/img/<filename>')
def img_static(filename):
    return static_file(filename, root='./static/img')


@route('/css/<filename>')
def img_static(filename):
    return static_file(filename, root='./static/css')



@route('/')
def index():
	return template('index')

@route('/site',method='POST')
def site():
	embed=[]
	fb=request.POST.get('fb')
	insta=request.POST.get('insta')
	twitter=request.POST.get('twitter')	
	print type(fb)
	post_total=[]
	video_total=[]
	photo_total=[]
	if twitter:
		
		for link in twitter:
			twitter_dict = ggtwitter.GGTwitter(page=link,seconds=60*60*24*5, no_of_posts=5) 	
			twitter_dict = twitter_dict.final_data
			post_total+=twitter_dict['post']
			#video_total+= twitter_dict['video']
		 	photo_total += twitter_dict['photo']
	if fb : 
		fb=fb.replace(' ','').split(',')
		for link in fb:
			fb_dict = ggfb.GGFB(url=link,seconds=60*60*24*5, no_of_posts=5)
		 	fb_dict=fb_dict.fun_all()
		 	post_total += fb_dict['post']
		 	
	if insta:	 	
		insta=insta.split(',')
		for link in insta:
			insta_dict = gginsta.GGInsta(page=link,seconds=60*60*24*5, no_of_posts=5)
			insta_dict = insta_dict.generate_list()
			video_total+= insta_dict['video']
		 	photo_total += insta_dict['photo']



	final_dict=post_total+video_total+photo_total


	final_dict = sorted(final_dict, key=lambda k: k['timestamp'], reverse=True)
	for post in final_dict:
			if post['channel']=='fb':
				#a,b=post['embed'].split('_')
				embed.append(['fb',post['embed']])
			elif post['channel']=='insta':
				embed.append(['insta',post['url']])
			elif post['channel']=='twitter':
				embed.append(['twitter',post['url']])

			

	
	
	return template('stream',emb=embed)


if __name__=='__main__':
	run(debug=True,port=8866,reloader=True)	
