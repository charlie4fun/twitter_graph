import json


def load_tweets(files_count):
    """
    creates list of dicts containing following info about a tweet:
    {
    'user': <USER_ID>,
    'quoted': <USER_ID>,
    'retweeted': <USER_ID>,
    'mentioned': <USER_IDS_LIST>,
    'replied': <USER_ID>,
    }
    """
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
            if not tweet.get('user'):
                # requests exceeded message: {'limit': {'track': 1, 'timestamp_ms': '1492780990438'}}
                print("WARNING!!! File name: twitter_data_%s.txt" % i)
                print("tweet: %s" % tweet)
            else:
                record = {'user': tweet['user']['id'], }

                # retweetee is always in mentioned
                # if tweet.get('retweeted_status'):
                #    record['retweeted'] = tweet['retweeted_status']['user']['id']

                if tweet['entities'].get('user_mentions'):
                    mentioned = [user['id'] for user in tweet['entities']['user_mentions']]
                    record['mentioned'] = mentioned

                # TODO: tests for quoted and replied duplication in mentioned

                if tweet.get('quoted_status') and\
                        (tweet.get('quoted_status') not in record.get('mentioned', [])):
                    record['quoted'] = tweet['quoted_status']['user']['id']

                if tweet.get('in_reply_to_user_id') and\
                        (tweet.get('in_reply_to_user_id') not in record.get('mentioned', [])):
                    record['replied'] = tweet['in_reply_to_user_id']

                if len(record) >= 2:  # check if tweet have out-degree links at all
                    records.append(record)

    return records


def merge_links(records):  # requires testing!!!!
    """
    creates dict of interactions:
    {<IN_DEGREE_USER_ID>_<OUT_DEGREE_USER_ID>: <NUMBER_OF_INTERACTIONS>,}
    """
    interactions = {}
    for record in records:
        user = record['user']
        interactions[user] = []
        if record.get('mentioned'):
            interactions[user] = record['mentioned']
        if record.get('quoted'):
            interactions[user].append(record['quoted'])
        if record.get('replied'):
            interactions[user].append(record['replied'])

    edges = {}
    for out_degree, in_degrees in interactions.items():
        for in_degree in in_degrees:
            edge = '%s_%s' % (in_degree, out_degree)
            if edges.get(edge):
                edges[edge] += 1
            else:
                edges[edge] = 1

    return edges


# TODO: add flush to shelve-file after each txt-file {user: [in-degree links], }
