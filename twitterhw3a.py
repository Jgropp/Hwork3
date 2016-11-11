# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "hvhMYZ99LcHrClJIQBI0kE6Gf",
    "consumer_secret"     : "xjhLHGUwwMHeQlfBFi9G8A5gYS29cQKX0KOo0ulHjXDjw6jXHM",
    "access_token"        : "242105174-V8UMay30MTfwhITBCpslZkxy1qHCwG5eiKJngTlG",
    "access_token_secret" : "TktnkmDXa07vYOWZHNq9Faa04r8LwJLKfgZMJtvXP3txY" 
    }

  api = get_api(cfg)
 
  tweet = "#UMSI-206 #Proj3"
  status = api.update_with_media("smiley-face.jpg", tweet) #Tweets out picture from python

if __name__ == "__main__":
  main()

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

#References: http://nodotcom.org/python-twitter-tutorial.html


