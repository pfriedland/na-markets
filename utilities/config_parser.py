import json
import logging
class ConfigParser:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.parse()

    def parse(self):
        try:
            return json.loads(self.file_name)
        except Exception as e:
            #TODO logging statement
            raise e