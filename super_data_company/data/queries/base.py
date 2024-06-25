from abc import ABC, abstractmethod


class BaseEngine(ABC):
    @abstractmethod
    def filter(self, records, query_params):
        pass
