import json
# import pandas

FILES_COUNT = 14

'''
creates list of dicts containing following info about a tweet

{
'user': <USER_ID>,
'quoted': <USER_ID>,
'retweeted': <USER_ID>,
'mentioned': <USER_IDS_LIST>,
'replied': <USER_ID>,
}
'''

records = []

for i in range(FILES_COUNT+1):

    tweets_data = []
    tweets_file = open('twitter_data_%s.txt' % i)
    for line in tweets_file:
        try:
            tweet_data = json.loads(line)
            tweets_data.append(tweet_data)
        except json.decoder.JSONDecodeError:
            continue

    for tweet in tweets_data:  # collection of all out-degree links in each tweet
        record = {'user': tweet['user']['id'], }
        if tweet['quoted_status']:
            record['quoted'] = tweet['quoted_status']['user']['id']
        if tweet['retweeted_status']:
            record['retweeted'] = tweet['retweeted_status']['user']['id']
        if tweet['entities']['user_mentions']:
            record['mentioned'] = tweet['entities']['user_mentions']
        record['replied'] = tweet.get['in_reply_to_user_id']
        if len(record) >= 2:  # check if tweet have out-degree links at all
            records.append(record)

    # TODO: add flush to shelve-file after each txt-file {user: [in-degree links], }
