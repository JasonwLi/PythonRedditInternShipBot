import praw
import time
import datetime
import config
def bot_login():
    r = praw.Reddit(username = config.username,
	   	password = config.password,
	        client_id = config.client_id,
                client_secret = config.client_secret,
	        user_agent = "test_bot v.01")
    return r
def start_bot(r):
	lines =["List of potential internships/co-ops"]	
	pattern  = "%d/%m/%y"
	today = time.strftime(pattern)
	y = datetime.datetime.now() - datetime.timedelta(days = 1)
	yesterday = y.strftime(pattern)
	date1 = int(time.mktime(time.strptime(today, pattern)))
	date2 = int(time.mktime(time.strptime(yesterday, pattern)))

	subreddits = [r.subreddit('cscareerquestions')]
	subreddits.append(r.subreddit('internships'))
	subreddits.append(r.subreddit('jobhunting'))
	for sub in subreddits:
		for posts in sub.submissions(date2,date1):
			if "intern" or "co-op" in posts.selftext or posts.title:
				lines.append(posts.shortlink)
			##print(url)
	msg = '\n'.join(urls)
	user = ''
	r.redditor(user).message('Intern',msg)

		
r = bot_login()
start_bot(r)

