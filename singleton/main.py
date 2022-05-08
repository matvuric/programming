import requests
from xml.etree import ElementTree as elTree


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class CurrenciesList(Singleton):
    def get_currencies(self, currencies_ids_lst=None):
        if currencies_ids_lst is None:
            currencies_ids_lst = ['R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589', 'R01625', 'R01670',
                                  'R01700J', 'R01710A']
        cur_res_str = requests.get("https://www.cbr.ru/scripts/XML_daily.asp")
        result = {}
        cur_res_xml = elTree.fromstring(cur_res_str.content)
        valutes = cur_res_xml.findall("Valute")

        for _v in valutes:
            valute_id = _v.get('ID')
            if str(valute_id) in currencies_ids_lst:
                valute_cur_val = _v.find('Value').text
                valute_cur_name = _v.find('Name').text
                result[valute_id] = (valute_cur_val, valute_cur_name)
        return result


print(CurrenciesList().get_currencies())
