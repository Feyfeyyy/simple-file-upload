import csv

from .base import BaseParser


class CSVParser(BaseParser):
    def parse(self, data):
        return list(csv.DictReader(data.read().decode("utf-8").splitlines()))
