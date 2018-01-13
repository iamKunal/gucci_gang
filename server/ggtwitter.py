from twitter import Twitter,OAuth,TwitterHTTPError
import json
from datetime import datetime
from calendar import timegm
import time
CURRENT_TIME =timegm(datetime.utcnow().utctimetuple())
# from google.cloud import language
# from google.cloud.language import enums
# from google.cloud.language import types
class GGTwitter:
    ACCESS_TOKEN="872398728589488128-mWxShD0jnYAhHAyhvlsCHJozPThrsu1"
    ACCESS_SECRET="duY1j0Tx4YfOxuaG0W8R5vNivanErBOcdjgrASq5FNor2"
    CONSUMER_KEY="NSpQnH2ScuFcJ5iA5Boso0NuD"
    CONSUMER_SECRET="gIuCjz1b0fXB5sDlbXJldpGbzwCYs197WUWWVPmtPCG2L6q6H1"
    no_of_posts=None
    weight=None
    page=None
    seconds=None
    final_data = {'post': [],'photo': [],'video': []}
    def __init__(self,page,seconds,no_of_posts):
        self.page=page
        self.seconds=seconds
        self.no_of_posts=no_of_posts
        oauth=OAuth(self.ACCESS_TOKEN,self.ACCESS_SECRET,self.CONSUMER_KEY,self.CONSUMER_SECRET)
        twitter=Twitter(auth=oauth)
        user_name=self.get_user_name(page)
        tweets=twitter.statuses.user_timeline(screen_name=user_name,count=no_of_posts)
        for tweet in tweets:
            temp_dict={}
            temp_dict["url"]=None
            temp_dict["attachment"]=None
            temp_dict["timestamp"]=tweet[unicode("created_at")].encode("utf-8")
            curr_time=time.strptime(temp_dict["timestamp"], '%a %b %d %H:%M:%S +0000 %Y')
            temp_dict["timestamp"]=timegm(curr_time)
            if(temp_dict["timestamp"]-CURRENT_TIME>seconds):
                break
            if len(tweet[unicode("entities")][unicode("urls")])>0:
                temp_dict["url"]=tweet[unicode("entities")][unicode("urls")][0]["url"].encode("utf-8")
            
            temp_dict["channel"]="twitter"
            temp_dict["id"]=int(tweet[unicode("id")])    
            temp_dict["caption"]=tweet[unicode("text")].encode("utf-8")
            # try:
            #     print(temp_dict["caption"],self.classify(temp_dict["caption"]))
            # except:
            #     print("error")
            temp_dict["likes"]=int(tweet[unicode("favorite_count")])
            temp_dict["retweets"]=int(tweet[unicode("retweet_count")])
            temp_dict["comment"]=tweet[unicode("text")].encode("utf-8")
            temp_dict["type"]="post"
            if(unicode("media") in tweet[unicode("entities")]):
                if(len(tweet[unicode("entities")][unicode("media")])>0):
                    temp_dict["type"]=tweet[unicode("entities")][unicode("media")][0]["type"].encode("utf-8")
                    temp_dict["attachment"]=tweet[unicode("entities")][unicode("media")][0]["media_url"].encode("utf-8")
            self.final_data[temp_dict["type"]].append(temp_dict)
    def evaluate_weight(self):
        self.weight=0
        return self.weight
    def get_user_name(self,url):
        return url
        end_point=len(url)-1
        while(bool(end_point>=0) and bool(url[end_point]!='/')):
            end_point=end_point-1
        if(end_point<0):
            raise "Can't extract user-name from web-address"
        return url[end_point+1:]
    
    # def classify(self,text):
    #     try:
    #         client = language.LanguageServiceClient()
    #         document = types.Document(
    #             content=text,
    #             type=enums.Document.Type.PLAIN_TEXT)
    #         response = client.classify_text(
    #              document=document
    #          )
    #         return response.categories[0].name
    #     except:
    #         return ""
#run=GGTwitter("https://twitter.com/WittyFeed",60*60*24*30,100)
