import json

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


def load_tweets(files_count):
    records = []

    for i in range(files_count):

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
            if tweet.get('quoted_status'):
                record['quoted'] = tweet['quoted_status']['user']['id']

            if tweet.get('retweeted_status'):  # TODO: check if retweetee would always be in mentioned
                record['retweeted'] = tweet['retweeted_status']['user']['id']

            if tweet['entities'].get('user_mentions'):
                mentioned = [user['id'] for user in tweet['entities']['user_mentions']]
                record['mentioned'] = mentioned

            if tweet.get('in_reply_to_user_id'):
                record['replied'] = tweet['in_reply_to_user_id']

            if len(record) >= 2:  # check if tweet have out-degree links at all
                records.append(record)

    return records

    # TODO: add flush to shelve-file after each txt-file {user: [in-degree links], }
