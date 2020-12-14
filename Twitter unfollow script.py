!pip install python-twitter
import twitter
import pickle
import os
import pandas
import time

if not os.path.exists('secret_twitter_credentials.pkl'):
    Twitter={}
    Twitter['Consumer Key'] = ''
    Twitter['Consumer Secret'] = ''
    Twitter['Access Token'] = ''
    Twitter['Access Token Secret'] = ''
    with open('secret_twitter_credentials.pkl','wb') as f:
        pickle.dump(Twitter, f)
else:
    Twitter=pickle.load(open('secret_twitter_credentials.pkl','rb'))

api = twitter.Api(Twitter['Consumer Key'],
                  Twitter['Consumer Secret'],
                  Twitter['Access Token'],
                  Twitter['Access Token Secret'])

friends = api.GetFriends()
followers = api.GetFollowers()

friend_IDs = []
for i in range(len(friends)):
    friend_IDs.append(friends[i].id)

followers_IDs = []
for i in range(len(followers)):
    followers_IDs.append(followers[i].id)

for i in range(len(friend_IDs)):
    if friend_IDs[i] not in followers_IDs:
        api.DestroyFriendship(user_id = friend_IDs[i])
    time.sleep(0.25)
