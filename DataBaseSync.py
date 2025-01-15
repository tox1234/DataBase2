"""
Author: Ido Shema
Date: 13/01/2025
Description: simple dataBase class that supports threading using WinAPI synchronization primitives.
"""
import time
from DataBaseFile import DataBaseFile
import win32event

MAX = 10


class DataBaseSync(DataBaseFile):
    def __init__(self, dict_=None):
        super().__init__(dict_)

        if dict_ is None:
            dict_ = {}

        self.write_mutex = win32event.CreateMutex(None, False, None)
        self.read_semaphore = win32event.CreateSemaphore(None, MAX, MAX, None)

    def set_value(self, key, val):
        """
            Sets the value and the key in the database
            :param val: value of key
            :param key: the key
            :return: None
        """
        win32event.WaitForSingleObject(self.write_mutex, win32event.INFINITE)

        try:
            for _ in range(MAX):
                win32event.WaitForSingleObject(self.read_semaphore, win32event.INFINITE)

            super().set_value(key, val)
            time.sleep(2)
        finally:
            for _ in range(MAX):
                win32event.ReleaseSemaphore(self.read_semaphore, 1)

            win32event.ReleaseMutex(self.write_mutex)

    def get_value(self, key):
        """
            Gets the value of a certain key
            :param key: the key
            :return: value of a certain key
        """
        win32event.WaitForSingleObject(self.read_semaphore, win32event.INFINITE)
        try:
            value = super().get_value(key)
            time.sleep(2)
        finally:
            win32event.ReleaseSemaphore(self.read_semaphore, 1)

        return value

    def delete_value(self, key):
        """
            Deletes the value of a certain key
            :param key: the key
            :return: None
        """
        win32event.WaitForSingleObject(self.write_mutex, win32event.INFINITE)

        try:
            for _ in range(MAX):
                win32event.WaitForSingleObject(self.read_semaphore, win32event.INFINITE)

            super().delete_value(key)
        finally:
            for _ in range(MAX):
                win32event.ReleaseSemaphore(self.read_semaphore, 1)

            win32event.ReleaseMutex(self.write_mutex)
