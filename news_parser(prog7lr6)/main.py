import re
import bs4
import requests
from bs4 import BeautifulSoup
import string
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
import wordcloud


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
    news_list = bs.find('td', {'class': 'blockwh'}).find_all(href=re.compile('^/news/07-10-2022_4/'))
    for i in news_list:
        new_html(dom + i['href'])


def new_html(url):
    bs = BeautifulSoup(requests.get(url).text, 'html.parser')
    text_list = bs.find('td', {'class': 'blockwh'}).find_all('p')
    text = ''
    for i in text_list:
        content = i.contents
        if len(content) > 1:
            for j in content:
                if type(j) is bs4.element.Tag:
                    text += j.string.lower()
                else:
                    text += j.lower()
        else:
            p = i.string
            if p is not None:
                text += p.lower()
    text_processing(text)


def text_processing(text):
    text = 'пваыпвыап ывапывапывап ывапывапыва ывапывапывап выапывапывап ывапывапывап, апывапыва. ывапываповыап. Привет'
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)
    print(doc.spans)
    # for span in doc.spans:
    #     span.normalize(morph_vocab)
    #
    # print({_.text: _.normal for _ in doc.spans})


def remove_chars_from_text(text, chars):
    return "".join([ch for ch in text if ch not in chars])


dom = 'https://www.herzen.spb.ru'
main_html('https://www.herzen.spb.ru/main/news/')

