import nltk
from nltk.chat.util import Chat, reflections
from newspaper import Article
nltk.download('punkt')

class searchbot:

    def bot(self, keyword):
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")
        query = keyword
        links = []
        content = ""
        for j in search(query, tld="com", num=15, stop=15, pause = 2):
            links.append(j)
        summary = {}
        description = {}
        length ={}
        for link in links:
            try:
                article = Article(link)
                article.download()
                article.parse()
                article.nlp()
                text = article.text
                if(len(text.split())) <50:
                    continue
                summary[link] = article.summary
                description[link] = text[0:3000]
                length[link] = len(text.split())
            except:
                pass
        return (summary, description, length)
