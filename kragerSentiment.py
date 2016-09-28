# Sentiment.py
# Demonstrates connecting to the twitter API and accessing the twitter stream
# Author: Andrew Krager
# Version 1.2
# Date: September 9, 2016

import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

print 'Example 1'
print 'Establish Authentication Credentials'
CONSUMER_KEY = 'ApCqPQzcmC3qMAUkjSWuE51vC'
CONSUMER_SECRET = 'b6gDEoKI64plTyJRTHc1YNDfqkGCzu90veFrKXV48LC4ZZzYge'
OAUTH_TOKEN = '1594584031-6RdeCdmgfZc0jF2JwSDMLl3xGMattNLUy3WQezO'
OAUTH_TOKEN_SECRET = 'jqhcBcT8LwxpG3hphYLgScru5mOLkGGSnWXlpog5nJCJp'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# XXX: Set this variable to a trending topic,
# or anything else for that matter. The example query below
# was a trending topic when this content was being developed
# and is used throughout the remainder of this chapter.

#q = '#MentionSomeoneImportantForYou'
q = raw_input('Enter a search term: ')
q2 = raw_input('Enter a second search term: ')
#print q
#raw_input("Press Enter to continue")

count = 1000

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

search_results2 = twitter_api.search.tweets(q=q2, count=count)

statuses2 = search_results2['statuses']


# Iterate through 5 more batches of results by following the cursor

for _ in range(5):
    print "Length of statuses", len(statuses)
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError, e: # No more results when next_results doesn't exist
        break

    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])

    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

for _ in range(5):
    print "Length of statuses", len(statuses2)
    try:
        next_results2 = search_results2['search_metadata']['next_results']
    except KeyError, e: # No more results when next_results doesn't exist
        break

    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs2 = dict([ kv.split('=') for kv in next_results2[1:].split("&") ])

    search_results2 = twitter_api.search.tweets(**kwargs)
    statuses2 += search_results2['statuses']
print 'Example 9. Sentiment Analysis on the search term from Example 5'
sent_file = open('AFINN-111.txt')

scores = {} # initialize an empty dictionary
for line in sent_file:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.

score = 0
for word in words:
    uword = word.encode('utf-8')
    if uword in scores.keys():
        score = score + scores[word]
scores2 = {} # initialize an empty dictionary
for line in sent_file:
    term2, score2  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores2[term2] = int(scores2)  # Convert the score to an integer.

score = 0
for word in words:
    uword2 = word.encode('utf-8')
    if uword2 in scores2.keys():
        score2 = score2 + scores2[word]
if score > score2:
    print 'The first search term has a more postive sentiment with a score of ', score
    print 'The second search term had a score of ', score2

elif score2 > score:
    print 'The second search term has a more postive sentiment with a score of ', score2
    print 'The first search term had a score of ', score
