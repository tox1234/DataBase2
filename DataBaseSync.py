"""
Author: Ido Shema
Date: 01/11/2024
Description: simple dataBase class that support threading and processing
"""
import time
from DataBaseFile import DataBaseFile
import threading
import multiprocessing
MAX = 10


class DataBaseSync(DataBaseFile):
    def __init__(self, mode, dict_=None):
        super().__init__(dict_)

        if dict_ is None:
            dict_ = {}

        if mode == 'Thread':
            self.write = threading.Lock()
            self.read = threading.Semaphore(MAX)

        elif mode == 'Process':
            self.write = multiprocessing.Lock()
            self.read = multiprocessing.Semaphore(MAX)

    def set_value(self, key, val):
        """
            sets the value and the key in the database
            :param val: value of key
            :param key: the key
            :return: None
        """
        with self.write:

            for i in range(MAX):
                self.read.acquire()

            super().set_value(key, val)
            time.sleep(2)

        for i in range(MAX):
            self.read.release()

    def get_value(self, key):
        """
            gets the value of a certain key
            :param key: the key
            :return: value of a certain key
        """
        with self.read:
            value = super().get_value(key)
            time.sleep(2)
        return value

    def delete_value(self, key):
        """
            deletes the value of a certain key
            :param key: the key
            :return: None
        """
        with self.write:

            for i in range(MAX):
                self.read.acquire()

            super().delete_value(key)

        for i in range(MAX):
            self.read.release()

