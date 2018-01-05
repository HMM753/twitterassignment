#This code searches for tweets with a particuar keyword and writes certain fields into a CSV file
import sys, csv, twitter
import jsonpickle
import os
import tweepy
import pprint
# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler('suAsKeWF9Q0zKL2EIbWwlFM5E', 'MiC8zApiJZkGSY56bw0t4x34mM6JX9xiSwbLGCxY7nh9abT534')
api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)


if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
def clean(val):
	clean = ""
	if val:
		clean = val.encode('utf-8')
	return clean

searchQuery = '@taylorswift13'  # this is what we're searching for
maxTweets = 1000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'twitter_res.csv' # We'll store the tweets in a CSV file.
csvfile = open(fName, 'w');
#csvfile = open('paris_data_new.csv', 'w')
csvwriter = csv.writer(csvfile)

count=0

# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = 'taylorswift13'

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1
tweetCount = 0

#Since Id helps us get the tweets since a particular id. This helps us prevent overlapping tweets
with open(fName, 'wb') as csvfile:
    while tweetCount < maxTweets:
        pprint.pprint(tweetCount)
        try:
            # if (max_id <= 0):
            #     if (not sinceId):
            #         new_tweets = api.search(q=searchQuery, count=tweetsPerQry) #Use Twitter's search API
            #     else:
            #         new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
            #                                 since_id=sinceId) #Search from sinceId onwards
            # else:
            #     if (not sinceId):
            #         new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
            #                                 max_id=str(max_id - 1))
            #     else:
            #         new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
            #                                 max_id=str(max_id - 1),
            #                                 since_id=sinceId)
            new_tweets = api.user_timeline(id='taylorswift13')
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                #pprint.pprint(tweet)
                #raise SystemExit
                csvwriter.writerow([tweet.created_at,
                clean(tweet.user.screen_name),
                clean(tweet.text),
                tweet.user.created_at,
                tweet.user.followers_count,
                tweet.user.friends_count,
                tweet.user.statuses_count,
                clean(tweet.source),
                clean(tweet.user.location),
                tweet.user.geo_enabled,
                tweet.user.lang,
                clean(tweet.user.time_zone),
                tweet.retweet_count
                ]);
				#csvwriter.writerow([tweet.user.screen_name.encode('utf-8'),tweet.text.encode('utf-8'), tweet.retweet_count,tweet.created_at]);
				#f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        #'\n')
            tweetCount += len(new_tweets)
            #print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except Exception as e:
            # Just exit if any error
            print("some error : " + str(e))
            pass

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
