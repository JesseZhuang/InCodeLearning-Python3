import logging

from pymongo import MongoClient

from stock.model.stock import Stock

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('pymongo').setLevel(logging.ERROR)


class MongoWrapper:
    def __init__(self):
        uri = "mongodb://localhost:27017/"
        self.client = MongoClient(uri)

    def get_collection(self, db: str, collection_name: str):
        db = self.client[db]
        return db.get_collection(collection_name)  # create if not existing

    def create_collection(self, db: str, collection_name: str):
        db = self.client[db]  # db will be created if not existing
        db.create_collection(collection_name)  # maybe lazy

    def get_client(self):
        return self.client

    def get_db(self, db: str):
        return self.client[db]

    def insert_watchlist_stock(self, db: str, collection: 'str', stock: Stock):
        c = self.get_collection(db, collection)
        res = c.insert_one(stock.__dict__)
        logger.info(f"inserted one stock, res: {res}")

    def query_watchlist_stock(self, db: str, collection: 'str', ticker: str) -> Stock | None:
        c = self.get_collection(db, collection)
        res = c.find_one({'_id': ticker})
        if not res: return None
        logger.info(f"found one stock, res: {res}")
        return Stock(**res)
