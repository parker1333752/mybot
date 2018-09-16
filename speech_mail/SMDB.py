from pymongo import MongoClient

class SMDB:
    host = 'localhost'
    port = 27017

    def __init__(self):
        pass

    def open(self):
        self.conn = MongoClient(self.host, self.port)
        self.db = self.conn.

