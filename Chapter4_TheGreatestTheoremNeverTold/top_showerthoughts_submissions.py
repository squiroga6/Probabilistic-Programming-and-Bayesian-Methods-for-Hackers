import sys

import numpy as np
from IPython.core.display import Image

import praw
import json

with open("../config.json", "r") as read_file:
    data = json.load(read_file)

# reddit = praw.Reddit("BayesianMethodsForHackers")

reddit = praw.Reddit(client_id=data['user_id'],
                     client_secret=data['secret'],
                     user_agent="Bayes methods for hackers course",
                     username=data['username'],
                     password=data['password'])

subreddit  = reddit.subreddit("showerthoughts")

top_submissions = subreddit.top(limit=100)

n_sub = int( sys.argv[1] ) if sys.argv[1] else 1

i = 0
while i < n_sub:
    top_submission = next(top_submissions)
    i+=1

top_post = top_submission.title

upvotes = []
downvotes = []
contents = []

# for sub in top_submissions:
#     try:
#         ratio = reddit.get_submission(sub.permalink).upvote_ratio
#         ups = int(round((ratio*sub.score)/(2*ratio - 1)) if ratio != 0.5 else round(sub.score/2))
#         upvotes.append(ups)
#         downvotes.append(ups - sub.score)
#         contents.append(sub.title)
#     except Exception as e:
#         continue

for sub in top_submissions:
    try:
        ratio = sub.upvote_ratio
        ups = int(round((ratio*sub.score)/(2*ratio - 1)) if ratio != 0.5 else round(sub.score/2))
        upvotes.append(sub.ups)
        downvotes.append(ups - sub.score)
        contents.append(sub.title)
    except Exception as e:
        raise e
        
votes = np.array( [ upvotes, downvotes] ).T