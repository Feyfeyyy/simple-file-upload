import json

from .base import BaseParser


class JSONParser(BaseParser):
    def parse(self, data):
        return json.load(data)
