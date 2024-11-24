from datetime import datetime

from pymongo import MongoClient

from data.model.stock import Stock


class MongoWrapper:
    def __init__(self):
        uri = "mongodb://localhost:27017/"
        self.client = MongoClient(uri)

    def create_collection(self, db: str, collection_name: str):
        db = self.client[db]  # db will be created if not existing
        db.create_collection(collection_name)  # maybe lazy

    def get_collection(self, db: str, collection_name: str):
        db = self.client[db]
        return db.get_collection(collection_name)  # create if not existing

    def get_client(self):
        return self.client

    def get_db(self, db: str):
        return self.client[db]


def test_ping(mongo_client):
    try:
        mongo_client.admin.command("ping")
        print("Connected successfully")
        mongo_client.close()
    except Exception as e:
        raise Exception("The following error occurred: ", e)


def test_collection(mongo_wrapper):
    test_db = mongo_wrapper.get_db("test_db_jz1")
    c = test_db.get_collection("test_c_jz1")
    return c


def test_insert(mongo_wrapper):
    c = test_collection(mongo_wrapper)
    apple = Stock('aapl', 'apple', 20, 'tech', 'mobile', 21.1, 4, 200000,
                  8.5, 1000, 0.23, datetime.today())
    res = c.insert_one(apple.__dict__)
    print(f"Inserted {res}")
    print(c.find_one({'_id': apple._id}))


def test_read(mongo_wrapper):
    c = test_collection(mongo_wrapper)
    apple = c.find_one({'_id': 'aapl'})
    print(type(apple))
    stock = Stock(**apple)
    print(stock)
    not_exist = c.find_one({'_id': 'not_exist'})
    print(not_exist)  # should be None


if __name__ == "__main__":
    wrapper = MongoWrapper()
    # client = wrapper.get_client()
    # test_ping(client)
    # test_insert(wrapper)  # duplicate key error if try to insert again
    test_read(wrapper)
