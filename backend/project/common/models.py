from django.db import models
from abc import *
from dataclasses import dataclass
import pandas as pd
import json
import googlemaps
from selenium import webdriver
from icecream import ic


@dataclass
class FileDTO(object):

    context: str
    fname: str
    dframe: object
    url: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def dframe(self) -> object: return self._dframe

    @dframe.setter
    def dframe(self, dframe): self._dframe = dframe

    @property
    def url(self) -> object: return self._url

    @url.setter
    def url(self, url): self._url = url


class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def dframe(self):
        pass


class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def new_file(self):
        pass

    @abstractmethod
    def csv(self):
        pass

    @abstractmethod
    def xls(self):
        pass

    @abstractmethod
    def json(self):
        pass

    @abstractmethod
    def csv_header(self):
        pass


class ScraperBase(metaclass=ABCMeta):
    @abstractmethod
    def driver(self):
        pass


class Printer(PrinterBase):

    def dframe(self, this):

        n = 10
        print('*' * 100)
        ic(type(this))
        ic(this.columns)
        ic(this.head(n))
        ic(this.isnull().sum())
        '''
        print('*' * 100)
        print(f'1. Target 의 Type 은 {type(this)}')
        print(f'2. Target 의 column 은 {this.columns}')
        print(f'3. Target 의 상위 {n}개 행은 \n{this.head(n)}')
        print(f'4. Target null 의 개수 \n{this.isnull().sum()}개')
        '''


class Reader(ReaderBase):
    def new_file(self, file) -> str:
        return file.context + file.fname

    def csv(self, file) -> object:
        return pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=',')

    def xls(self, file, header, usecols) -> object:
        return pd.read_excel(f'{self.new_file(file)}.xls', header=header, usecols=usecols)

    def json(self, file) -> object:
        return json.load(open(f'{self.new_file(file)}.json', encoding='UTF-8'))

    def csv_header(self, file, header, usecols) -> object:
        return pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=',', usecols=usecols)

    def gmaps(self) -> object:
        return googlemaps.Client(key='')


class Scraper(ScraperBase):

    def driver(self) -> object:
        return webdriver.Chrome('C:/Program Files/Google/Chrome/chromedriver')

    def auto_login(self):
        pass
