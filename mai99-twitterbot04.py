import tweepy
import time

print ('Loading mai99-twitterbot04 program...')

consumer_key = 'xxxxxxxxx'
consumer_secret = 'xxxxxxxxx'
access_token = 'xxxxxxxxx'
access_token_secret = 'xxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Last Saved ID Tweet 1069987299977420800 for testing.
FILE_NAME = 'last_seen_id.txt'
#Your username
specific_user = 'xxxxxxxxx'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def retweet():
    print('Retrieving newest tweet from twitter server...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    user = api.user_timeline(since_id = last_seen_id, screen_name = specific_user, tweet_mode='extended')
    for status in reversed(user):
        print (str(status.id) + ' - ' + status.full_text)
        last_seen_id = status.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        api.retweet(status.id)
        time.sleep(3)
    print('Retrieving newest tweet from twitter server is complete!')
    print('Restart mai99-twitterbot04 program...')
    time.sleep(3)
    print('<=============================================================>')

while True:
    retweet()