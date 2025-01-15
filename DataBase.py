"""
Author: Ido Shema
Date: 13/01/2025
Description: simple dataBase class
"""


class DataBase:
    def __init__(self, dict_):
        self.dict = dict_

    def set_value(self, key, val):
        """
            sets the value and the key in the database
            :param val: value of key
            :param key: the key
            :return: None
        """
        self.dict[key] = val

    def get_value(self, key):
        """
            gets the value of a certain key
            :param key: the key
            :return: value of a certain key
        """
        return self.dict.get(key, None)

    def delete_value(self, key):
        """
            deletes the value of a certain key
            :param key: the key
            :return: None
        """
        del self.dict[key]


if __name__ == '__main__':
    db = DataBase({"cyber": "cool"})

    db.set_value("cyber", "great")
    assert db.get_value("cyber") == "great", "get value failed or set value"
    assert db.get_value("nothing") is None, "get value failed if key doesn't exist"
    db.delete_value("cyber")
    assert db.get_value("cyber") is None, "delete value failed"

    print("success")
