import requests
from collections import Counter
import json


class APIHandler(object):
    def __init__(self, url: str, token: str):
        self.__url = url
        self.__token = token
        self.__all_games = []
        self.__json_object = None

    def get_all_games(self) -> list:
        """ Method will be finished and return list of elements when each element of
            the array has already been received.
        """
        flag = True
        uniques_games = set()
        while flag:
            try:
                respond = requests.get(self.__url + self.__token)
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err)
            if respond.status_code != 200:
                raise SystemExit(f"bad answer from service with code{respond.status_code}")
            games_list = respond.content.decode('utf-8')[:-1].split(';')
            if len(games_list) < 6:
                continue
            if len(uniques_games.intersection(set(games_list))) == 6:
                flag = False
            uniques_games.update(games_list)
            self.__all_games.extend(games_list)

        return self.__all_games

    def build_jason(self, games_list: list):
        """To build json object from list using Counter to count elements"""
        list_ = [{'gamename': key, 'number': value, } for key, value in Counter(games_list).items()]
        self.__json_object = json.dumps(list_)
        return self.__json_object

    @staticmethod
    def print_jason(json_object) -> None:
        """Output json """
        print(json_object)



