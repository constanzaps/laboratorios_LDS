
import praw
import numpy as np
def praw_reddit(nombre_subreddit = 'chile', n_hot = 1000):
  reddit = praw.Reddit(client_id='-w2hyFINxZ8T3g',
                     client_secret='zGPCI4s3g6Ic6AsRi7vIpP0NoxbFdw',
                     password='ClasesMDS7202',
                     user_agent='Clases',
                     username='DocenciaDataScience', check_for_async=False)
  subreddit  = reddit.subreddit(nombre_subreddit)
  votes, post, url = {}, {}, {}
  top_submissions = list(subreddit.hot(limit = n_hot))
  for it, top_n in enumerate(range(50, len(top_submissions),50)):
    top_n_submissions = top_submissions[:top_n]
    upvotes, downvotes, url[it], post[it] = [], [], [], []
    for submission in top_n_submissions:
        try:
            ratio = submission.upvote_ratio
            ups = int(round((ratio*submission.score)/(2*ratio - 1)) if ratio != 0.5 else round(submission.score/2))
            upvotes.append(ups)
            downvotes.append(ups - submission.score)
            post[it].append(submission.title)
            url[it].append(submission.url)
        except Exception as e:
            continue
    votes[it] = np.array([upvotes, downvotes]).T
  return votes, post, url
