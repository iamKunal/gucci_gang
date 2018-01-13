from bs4 import BeautifulSoup
from requests import get
import re

from boilerpipe.extract import Extractor


def get_text(url):
    if url is None:
        return None
    response = get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    data = soup.findAll(text=True)

    def visible(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title', 'meta']:
            return False
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        elif re.match('<.*>', str(element.encode('utf-8'))):
            return False
        return True

    result = filter(visible, data)
    result = filter(lambda x: x != '\n' and 'share on' not in x.lower(), result)
    return result


def get_tags(url):
    if url is None:
        return None
    response = get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    data = soup.findAll(text=True)
    metas = []
    for a in soup.find_all('meta', {'property': 'article:tag'}):
        s = a.get('content').encode('utf-8')
        if len(s) > len('--primarykeyword-'):
            if s[:len('--primarykeyword-')] == '--primarykeyword-':
                metas.append(s[len('--primarykeyword-'):])
            else:
                metas.append(s)
        else:
            metas.append(s)
    return metas


if __name__ == "__main__":
    # # txt = get_tags('https://www.buzzfeed.com/sahilrizwan/whatay-guy?utm_term=.whR4Nje00#.dhzWm2E55')
    # txt = get_text('https://www.wittyfeed.com/story/62599/things-indian-mother-does')
    # print "\n".join(txt)

    URL = 'https://www.wittyfeed.com/story/62599/things-indian-mother-does'
    URL = 'https://www.buzzfeed.com/sahilrizwan/whatay-guy?utm_term=.whR4Nje00#.dhzWm2E55'
    URL = 'http://www.dailymail.co.uk/news/article-5266131/Katie-Couric-breaks-silence-Matt-Lauer-sex-scandal.html'
    extractor = Extractor(extractor='ArticleExtractor', url=URL)

    print extractor.getText()
