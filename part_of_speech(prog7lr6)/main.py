import requests
import nltk
from collections import Counter
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def dedublicate(arr):
    n = []
    for i in arr:
        if i.lower() not in n:
            n.append(i.lower())
    return n


def sum_parts(arr):
    for i in range(1, len(arr)):
        if counts[arr[i]]:
            counts[arr[0]] += counts.get(arr[i])
            counts.pop(arr[i])


url = 'https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt'

tokenized_text = dedublicate(nltk.word_tokenize(requests.get(url).text))
tagged = nltk.pos_tag(tokenized_text)
counts = Counter(tag for word, tag in tagged)


sum_parts(['NN', 'NNS', 'NNP', 'NNPS'])
sum_parts(['JJ', 'JJS', 'JJR'])
sum_parts(['RB', 'RBS', 'RBR'])
sum_parts(['VBZ', 'VBP', 'VBN', 'VBG', 'VBD', 'VB'])


print(counts.most_common(5))