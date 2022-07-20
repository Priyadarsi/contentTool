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
        for link in links:
            try:
                article = Article(link)
                article.download()
                article.parse()
                article.nlp()
                summary[link] = article.summary
            except:
                pass
        return summary
