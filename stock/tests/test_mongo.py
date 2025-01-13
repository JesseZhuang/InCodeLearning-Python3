import logging
from datetime import datetime
from unittest import TestCase

from stock.client.mongo import MongoWrapper
from stock.model.stock import Stock

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class TestMongoWrapper(TestCase):

    def setUp(self):
        self.wrapper = MongoWrapper()
        self.client = self.wrapper.get_client()
        self.test_db = self.client['test_db_jz1']
        self.test_collection = self.test_db['test_c_jz1']
        self.test_ticker = 'aapl'

    def tearDown(self):
        self.client.close()

    def test_watchlist_stock(self):
        """test insert and query watchlist stock"""
        apple = Stock(self.test_ticker, 'apple', 20.1, 'tech', 'mobile', 21.1, 4, 200000.0, 1.1,
                      8.5, 1000, 15.23, 0.1, datetime.today(), 0.0)
        res = self.test_collection.insert_one(apple.__dict__)
        logger.info(f'inserted res: {res}')
        res = self.test_collection.find_one({'_id': res.inserted_id})
        logger.info(f'found res: {res}, type: {type(res)}')
        stock = Stock(**res)
        logger.info(f'found stock: {stock}')
        self.assertTrue(stock.id, self.test_ticker)
        self.test_collection.delete_one({'_id': self.test_ticker})

    def test_query_not_found(self):
        not_exist = self.test_collection.find_one({'_id': 'not_exist'})
        self.assertIsNone(not_exist)

    def test_delete(self):
        """delete if found, no error if not found"""
        res = self.test_collection.delete_one({'_id': 'aapl'})
        logger.info(f'deleted res: {res}')

    def test_ping(self):
        try:
            self.client.admin.command("ping")
            logger.info("Connected successfully")
        except Exception as e:
            raise Exception("The following error occurred: ", e)
