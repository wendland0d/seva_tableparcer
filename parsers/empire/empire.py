import requests
import json
import logging
import time

from fake_useragent import UserAgent


logging.basicConfig(level=logging.DEBUG)


class CSGOEMPIRE:

    def int(self):
        pass

    @staticmethod
    def parse(sesion: requests.Session = None, start_page: int = None, end_page: int = None , max_above: int = 12) -> dict and json:
        """
        CS:GO EMPIRE PARSER
        
        По результатам тестирования парсер отрабатывает 19! страниц без установки задержки запросов или без смены IP или PROXY

        :warn: Не работает на RU и NL ip-адресах (дополняется)
                
        :param sesion:
        :param start_page:
        :param end_page:
        :param max_above: Положительное или отрицательное число или ноль. Характеризует разницу между актуальной ценой и рекомендованной ценой предмета
        :return:
        """
        ua = UserAgent()
        basic_headers = {
            'accept': 'application/json, text/plain, */*',
            'user-agent': ua.random,
            'referer': 'https://csgoempire.com/withdraw'
        }

        if not sesion:
            sesion = requests.Session()
        sesion.headers.update(basic_headers)

        if not start_page:
            start_page = 1
        if not end_page:
            end_page = sesion.get(
                'https://csgoempire.com/api/v2/trading/items?per_page=160&page=1&price_max_above=15&auction=no&sort'
                '=desc&order=market_value').json()[
                'last_page']

        data = {}

        for i in range(start_page, end_page + 1):
            try:
                response = sesion.get(
                    f'https://csgoempire.com/api/v2/trading/items?per_page=160&page={i}&price_max_above={max_above}&auction=no&sort=desc&order=market_value').json()
                for j in range(160):
                    _ = {response['data'][j]['id']: {
                        'Name': response['data'][j]['market_name'],
                        'Price': response['data'][j]['market_value'] / 100,
                        'Float': response['data'][j]['wear'],
                        'Stickers': response['data'][j]['stickers']
                    }}

                    data.update(_)
                    logging.debug(f'-- {response["data"][j]["market_name"]} successfully parsed!')
                logging.info(f'Page {i} is over')
                time.sleep(3)
                logging.info(f'Sleeping for 3 second between requests')
                with open('empire.json', 'w') as f:
                    json.dump(data, f)
            except requests.exceptions.JSONDecodeError as err:
                logging.warning(f'Connecntion aboreted on page {i}. Error - {err}')
                with open('empire.json', 'w') as f:
                    json.dump(data, f)
                break

        return data

    def json_to_db():
        pass 



CSGOEMPIRE.parse()