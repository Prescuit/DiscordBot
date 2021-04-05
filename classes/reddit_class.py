from scripts.api.reddit_api import getRandomPostImage, getPost
class FetchReddit:
    def __init__(self, name):
        self.name = name
        #self.description = description

    async def execute(self):
        rand_post = await getRandomPostImage(self.name)
        return rand_post

    async def getTopPost(self, top):
        post = await getPost(self.name, top)
        return post