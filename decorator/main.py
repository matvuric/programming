from time import time
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup


class BaseCurrenciesList:
    def get_currencies(self, currencies_ids_lst: list) -> dict:
        pass


class CurrenciesList(BaseCurrenciesList):
    def __init__(self):
        self.rates_available = False
        self.t = time()
        self.dt = datetime.now().day
        self.rates = None

    def get_currencies(self, currencies_ids_lst: list = None) -> dict:
        t = time()
        dt = datetime.today().day
        result = {}

        if self.rates_available:
            return self.rates

        if not self.rates_available or (t - self.t > 3600 or dt != self.dt):
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
            self.rates = result
            self.rates_available = True
        return result


class Decorator(BaseCurrenciesList):
    __wrapped_object: BaseCurrenciesList = None

    def __init__(self, currencies_lst: BaseCurrenciesList):
        self.__wrapped_object = currencies_lst

    @property
    def wrapped_object(self) -> BaseCurrenciesList:
        return self.__wrapped_object

    def get_currencies(self, currencies_ids_lst: list = None) -> dict:
        return self.__wrapped_object.get_currencies(currencies_ids_lst)


class ConcreteDecoratorJSON(Decorator):
    def get_currencies(self, currencies_ids_lst: list = None) -> str:
        return json.dumps(self.wrapped_object.get_currencies(currencies_ids_lst), ensure_ascii=False, indent=4)


class ConcreteDecoratorCSV(Decorator):
    def get_currencies(self, currencies_ids_lst: list = None) -> str:
        currency_data = self.wrapped_object.get_currencies(currencies_ids_lst)

        if type(currency_data) is str:
            currency_data = json.loads(currency_data)

        csv_data = "ID;Rate;Name\n"
        for currency, val in currency_data.items():
            csv_data += f'{currency};{val[0]};{val[1]}\n'
        csv_data = csv_data.rstrip()
        return csv_data


def show_currencies(currencies: BaseCurrenciesList):
    print(currencies.get_currencies())


if __name__ == "__main__":
    cur_list_dict = CurrenciesList()
    wrapped_cur_list = Decorator(cur_list_dict)
    wrapped_cur_list_json = ConcreteDecoratorJSON(cur_list_dict)
    wrapped_cur_list_csv = ConcreteDecoratorCSV(cur_list_dict)

    show_currencies(wrapped_cur_list_json)
    show_currencies(wrapped_cur_list_csv)
    show_currencies(wrapped_cur_list)
