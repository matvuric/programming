import json
import re
import requests
from bs4 import BeautifulSoup


def main_html(url):
    bs = BeautifulSoup(requests.get(url).text, 'html.parser')
    inst_list = bs.find('td', {'class': 'blockwh'}).div.ul.contents
    for item in inst_list:
        result.append({'inst_name': item.string, 'url': dom + item.a['href'], 'dep_list': []})


def atlas_html(url):
    bs = BeautifulSoup(requests.get(url).text, 'html.parser')
    dep_list = bs.find('td', {'class': 'body'}).div.ul.contents
    for item in dep_list:
        dep = []
        find = find_inst(item.a.string.lower().strip())
        if find is not None:
            for i in item.ul:
                if i.string.lower().strip().startswith('кафедра'):
                    manager = table_html(dom_atlas + i.a['href'])
                    if manager is not None:
                        dep.append({'dep_name': i.string.strip(), 'head_name': manager[0], 'email': manager[1]})
            result[find]['dep_list'] = dep


def table_html(url):
    bs = BeautifulSoup(requests.get(url).text, 'html.parser')
    table = bs.find_all(href=re.compile('teacher'))
    req = bs.find_all(class_='mm1')[2].string.split(', ')[0]
    for teacher in table:
        teacher_name = teacher.string.strip()
        if teacher_name == req:
            return [teacher_name, teacher_html(dom_atlas + teacher['href'])]


def teacher_html(url):
    bs = BeautifulSoup(requests.get(url).text, 'html.parser')
    return bs.find_all(href=re.compile('mailto:'))[0].string


def find_inst(inst):
    for j in range(len(result)):
        if (result[j])['inst_name'].lower().strip() == inst:
            return j


if __name__ == '__main__':
    dom = 'https://www.herzen.spb.ru'
    dom_atlas = 'https://atlas.herzen.spb.ru/'
    result = []
    main_html('https://www.herzen.spb.ru/main/structure/inst/')
    atlas_html('https://atlas.herzen.spb.ru/faculty.php')

    with open('parse.json', 'w') as f:
        f.write(json.dumps(result, ensure_ascii=False))
