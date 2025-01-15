"""
Author: Ido Shema
Date: 13/01/2025
Description: Simple database class that turns into a file using Windows API.
"""
from DataBase import DataBase
import win32file
import os
import json

FILE_PATH = "file.json"


class DataBaseFile(DataBase):
    def __init__(self, dict_=None):
        super().__init__(dict_ or {})
        self.dump()

    def dump(self):
        """
        Saves the database into a file using Windows API.
        """
        data = json.dumps(self.dict).encode('utf-8')
        handle = win32file.CreateFile(
            FILE_PATH,
            win32file.GENERIC_WRITE,
            win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE,
            None,
            win32file.CREATE_ALWAYS,
            0,
            None
        )
        try:
            win32file.WriteFile(handle, data)
        finally:
            win32file.CloseHandle(handle)

    def load(self):
        """
        Loads the data from a file using Windows API and updates the database.
        """
        if not os.path.exists(FILE_PATH):
            self.dict = {}
            return

        handle = win32file.CreateFile(
            FILE_PATH,
            win32file.GENERIC_READ,
            win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE,
            None,
            win32file.OPEN_EXISTING,
            0,
            None
        )
        try:
            _, data = win32file.ReadFile(handle, os.path.getsize(FILE_PATH))
            self.dict = json.loads(data.decode('utf-8'))
        finally:
            win32file.CloseHandle(handle)

    def set_value(self, key, val):
        """
        Sets the value for a key in the database.
        """
        self.load()
        super().set_value(key, val)
        self.dump()

    def get_value(self, key):
        """
        Gets the value for a key in the database.
        """
        self.load()
        return super().get_value(key)

    def delete_value(self, key):
        """
        Deletes a key-value pair from the database.
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

    print("Success")
