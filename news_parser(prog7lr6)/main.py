import re
import requests
from bs4 import BeautifulSoup
from collections import Counter
from natasha import (
    Segmenter,
    MorphVocab,

    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,

    PER,
    NamesExtractor,
    DatesExtractor,
    MoneyExtractor,
    AddrExtractor,

    Doc
)
from wordcloud import WordCloud
import matplotlib.pyplot as plt


segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)

names_extractor = NamesExtractor(morph_vocab)
dates_extractor = DatesExtractor(morph_vocab)
money_extractor = MoneyExtractor(morph_vocab)
addr_extractor = AddrExtractor(morph_vocab)


def main_html(url):
    bs = BeautifulSoup(requests.get(url).text, 'html.parser')
    news_list = bs.find('td', {'class': 'blockwh'}).find_all(href=re.compile('^/news/'))[:5]
    for i in news_list:
        news_html(dom + i['href'])


def news_html(url):
    bs = BeautifulSoup(requests.get(url).text, 'html.parser')
    try:
        text_list = bs.find('td', {'class': 'blockwh'}).find_all('p')
    except Exception as e:
        text_list = []
        print(url)
        print(e)
    text = ''
    for i in text_list:
        try:
            text += i.text
        except Exception as e:
            print(url)
            print(e)
    print(url + '\n')
    text_processing(text.strip(), url.split('/')[4])


def text_processing(text, news_date):
    with open(f'news_{news_date}.txt', 'w', encoding="utf-8") as f:
        f.write(text)
    f = open(f'news_{news_date}.txt', "r", encoding="utf-8")
    txt = f.read()

    doc = Doc(txt)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)

    for span in doc.spans:
        span.normalize(morph_vocab)

    for span in doc.spans:
        if span.type == PER:
            span.extract_fact(names_extractor)

    for token in doc.tokens:
        token.lemmatize(morph_vocab)

    count_names = Counter([_.normal for _ in doc.spans if _.fact])

    if count_names != Counter():
        wordcloud = WordCloud().generate_from_frequencies(count_names)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    count_words = Counter([_.lemma.capitalize() for _ in doc.tokens if _.pos == 'NOUN'])

    if count_words != Counter():
        wordcloud = WordCloud().generate_from_frequencies(count_words)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()


if __name__ == '__main__':
    dom = 'https://www.herzen.spb.ru'
    main_html('https://www.herzen.spb.ru/main/news/')
