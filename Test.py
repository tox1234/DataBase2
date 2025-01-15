"""
Author: Ido Shema
Date: 13/01/2025
Description: tests for database
"""
import threading
from DataBaseSync import DataBaseSync


class Test:
    def __init__(self):
        self.threads = []
        self.db = DataBaseSync({})

    def number1(self):
        self.db.set_value('cyber', 'cool')

    def number2(self):
        return self.db.get_value('cyber')

    def number3(self):
        thread1 = threading.Thread(target=self.db.get_value, args=('cyber',))
        thread2 = threading.Thread(target=self.db.set_value, args=('database', 'test'))
        thread1.start()
        self.threads.append(thread1)
        thread2.start()
        self.threads.append(thread2)
        for t in self.threads:
            t.join()

    def number4(self):
        thread1 = threading.Thread(target=self.db.set_value, args=('beginning', "ending"))
        thread2 = threading.Thread(target=self.db.get_value, args=('beginning',))
        thread1.start()
        self.threads.append(thread1)
        thread2.start()
        self.threads.append(thread2)
        for t in self.threads:
            t.join()

    def number5(self):
        for i in range(8):
            thread = threading.Thread(target=self.db.get_value, args=('cyber',))
            thread.start()
            self.threads.append(thread)

    def number6(self):
        for i in range(8):
            thread = threading.Thread(target=self.db.get_value, args=('cyber',))
            thread.start()
            self.threads.append(thread)

        thread1 = threading.Thread(target=self.db.set_value, args=('cyber', 'fun'))
        thread1.start()
        thread1.join()

        for j in range(8):
            thread = threading.Thread(target=self.db.get_value, args=('cyber',))
            thread.start()
            self.threads.append(thread)

        for t in self.threads:
            t.join()


test = Test()
test.number1()
test.number2()
test.number3()
test.number4()
test.number5()
test.number6()
