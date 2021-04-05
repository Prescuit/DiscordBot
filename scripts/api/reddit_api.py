import asyncpraw
import os

reddit = asyncpraw.Reddit(
    client_id=os.environ.get("R_CLIENT_ID"),
    client_secret=os.environ.get("R_SECRET"),
    password=os.environ.get("R_PASS"),
    user_agent="Discord Bot",
    username=os.environ.get("R_USER"),
)

reddit.read_only = True

async def getPost(sub, top):
  subreddit = await reddit.subreddit(sub, fetch=True)
  if (subreddit.over18 and not top):
    return "That sub is nsfw you perve"
  async for submission in subreddit.hot(limit=3):
    if submission.stickied:
      pass 
    elif submission.is_self:
      s = "**"+submission.title + "**\n" + submission.selftext
      return s
      break
    else:
      return submission.url
      break

async def getRandomPostImage(sub):
    subreddit = await reddit.subreddit(sub)
    submission = await subreddit.random()
    if not submission.is_self:
        return submission.url
    else:
      return await getRandomPostImage(sub)