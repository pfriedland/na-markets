import json
import logging

class ConfigParser:
    def __init__(self, file_name) -> None:
        self.file_name = file_name


    def parse(self):
        try:
            # open a json file for reading and print content using json.load
            with open(self.file_name, "r") as content:  
                return json.loads(content.read())
        except Exception as e:
            #TODO logging statement
            raise e