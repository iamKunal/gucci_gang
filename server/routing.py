from bottle import run,route,template,request,static_file
import ggtwitter , gginsta , ggfb

rate_dic={}

def total(fb,insta,twitter):
    
    post_total=[]
    video_total=[]
    photo_total=[]
    
    if twitter:
        twitter=twitter.replace(' ','').split(',')
        for link in twitter:
            twitter_dict = ggtwitter.GGTwitter(page=link,seconds=60*60*24*5, no_of_posts=10)     
            twitter_dict = twitter_dict.final_data
            post_total+=twitter_dict['post']
            #video_total+= twitter_dict['video']
            photo_total += twitter_dict['photo']
    if fb : 
        fb=fb.replace(' ','').split(',')
        for link in fb:
            fb_dict = ggfb.GGFB(url=link,seconds=60*60*24*5, no_of_posts=10)
            fb_dict=fb_dict.fun_all()
            post_total += fb_dict['post']
             
    if insta:         
        insta=insta.split(',')
        for link in insta:
            insta_dict = gginsta.GGInsta(page=link,seconds=60*60*24*5, no_of_posts=10)
            insta_dict = insta_dict.generate_list()
            video_total+= insta_dict['video']
            photo_total += insta_dict['photo']



    return post_total+video_total+photo_total


@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./static/js')


@route('/img/<filename>')
def img_static(filename):
    return static_file(filename, root='./static/img')


@route('/css/<filename>')
def img_static(filename):
    return static_file(filename, root='./static/css')


@route('/rate')
def rate():
    embed=[]
    final_dict=rate_dic
    final_dict = sorted(final_dict, key=lambda k: k['rate'], reverse=True)
    maxx=final_dict[0]['rate']
    for post in final_dict:
        if post['channel']=='fb':
            #a,b=post['embed'].split('_')
            embed.append(['fb',post['embed'],post['rate']*60,maxx*60])
        elif post['channel']=='insta':
            embed.append(['insta',post['url'],post['rate']*60,maxx*60])
        elif post['channel']=='twitter':
            embed.append(['twitter',post['url'],post['rate']*60,maxx*60])           

    
    
    return template('rate',emb=embed)


@route('/')
def index():
    return template('index')

@route('/site',method='POST')
def site():
    fb=request.POST.get('fb')
    insta=request.POST.get('insta')
    twitter=request.POST.get('twitter')
    final_dict=total(fb,insta,twitter)[:20]
    global rate_dic 
    rate_dic = final_dict    
    embed=[]
    

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
