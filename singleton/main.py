import requests
from xml.etree import ElementTree as elTree


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


class CurrenciesList(Singleton):
    @staticmethod
    def get_currencies(currencies_ids_lst=None):
        if currencies_ids_lst is None:
            currencies_ids_lst = ['R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589', 'R01625', 'R01670',
                                  'R01700J', 'R01710A']
        cur_res_str = requests.get("https://www.cbr.ru/scripts/XML_daily.asp")
        result = {}
        cur_res_xml = elTree.fromstring(cur_res_str.content)
        val = cur_res_xml.findall("Valute")
        for i in val:
            val_id = i.get('ID')
            if str(val_id) in currencies_ids_lst:
                val_cur_val = i.find('Value').text
                val_cur_name = i.find('Name').text
                result[val_id] = (val_cur_val, val_cur_name)
        return result


print(CurrenciesList().get_currencies())
