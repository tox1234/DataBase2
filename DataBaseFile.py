"""
Author: Ido Shema
Date: 01/11/2024
Description: simple dataBase class that turns into file
"""
from DataBase import DataBase
import pickle
import os

FILE_PATH = "file.pkl"


class DataBaseFile(DataBase):
    def __init__(self, dict_=None):
        super().__init__(dict_ or {})
        self.dump()

    def dump(self):
        """
            saves the database into a file
            :return: None
        """
        with open(FILE_PATH, 'wb') as file:
            pickle.dump(self.dict, file)

    def load(self):
        """
            gets the data from a file and puts it into database
            :return: None
        """
        with open(FILE_PATH, 'rb') as file:
            self.dict = pickle.load(file)

    def set_value(self, key, val):
        """
            sets the value and the key in the database
            :param val: value of key
            :param key: the key
            :return: None
        """
        self.load()
        super().set_value(key, val)
        self.dump()

    def get_value(self, key):
        """
            gets the value of a certain key
            :param key: the key
            :return: value of a certain key
        """
        self.load()
        return super().get_value(key)

    def delete_value(self, key):
        """
            deletes the value of a certain key
            :param key: the key
            :return: None
        """
        self.load()
        super().delete_value(key)
        self.dump()


if __name__ == '__main__':
    db_file = DataBaseFile({"cyber": "cool"})

    db_file.set_value("cyber", "great")
    assert db_file.get_value("cyber") == "great", "get value failed or set value"

    assert db_file.get_value("nothing") is None, "get value failed if key doesn't exist"

    db_file.delete_value("cyber")
    assert db_file.get_value("cyber") is None, "delete value failed"

    print("success")
