import requests
import nltk
from collections import Counter
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def func(l):
    n = []
    for i in l:
        if i.lower() not in n:
            n.append(i.lower())
    return n


url = 'https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt'


tokenized_text = func(nltk.word_tokenize(requests.get(url).text))
tagged = nltk.pos_tag(tokenized_text)
counts = Counter(tag for word, tag in tagged).most_common(5)
print(counts)