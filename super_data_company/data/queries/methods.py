from .base import BaseEngine


class ExactMatch(BaseEngine):
    def filter(self, records, query_params):
        for key, value in query_params.items():
            records = [record for record in records if record.data.get(key) == value]
        return records


class PartialMatch(BaseEngine):
    def filter(self, records, query_params):
        filtered_records = records
        for key, value in query_params.items():
            filtered_records = [
                record
                for record in filtered_records
                if key in record.data and value in str(record.data[key])
            ]
        return filtered_records
