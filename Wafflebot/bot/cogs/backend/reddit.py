import requests

class Reddit:

    def __init__(self):
        self.headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"}

    def random_meme(self):
        with requests.session() as s:
            d = s.get('https://www.reddit.com/r/memes/random/.json', headers = self.headers).json()[0]['data']['children'][0]['data']
            return {'title': d['title'], 'meme_url': f'https://reddit.com{d["permalink"]}', 'image_url':  d["url"], 'upvotes': d["ups"],
                    'downvotes': d["downs"], "comment_count": d["num_comments"]}