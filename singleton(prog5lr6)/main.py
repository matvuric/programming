import requests
from bs4 import BeautifulSoup


class Singleton(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance


class CurrenciesList(metaclass=Singleton):
    @staticmethod
    def get_currencies(currencies_ids_lst=None):
        if currencies_ids_lst is None:
            currencies_ids_lst = [
                'R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589',
                'R01625', 'R01670', 'R01700J', 'R01710A'
            ]
        cur_res_str = requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text
        result = {}
        cur_res_xml = BeautifulSoup(cur_res_str, 'html.parser')
        val = cur_res_xml.find_all("valute")
        for _v in val:
            valute_id = _v['id']
            if str(valute_id) in currencies_ids_lst:
                val_cur_val = _v.find('value').string
                val_cur_name = _v.find('name').string
                result[valute_id] = (val_cur_val, val_cur_name)
        return result
