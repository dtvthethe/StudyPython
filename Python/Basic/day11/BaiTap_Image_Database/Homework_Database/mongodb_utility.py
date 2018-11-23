import pymongo


class MongoUtility:

    def __init__(self, host, port, db_name):
        self.host = host
        self.port = port
        self.db_name = db_name

    def connect(self):
        return pymongo.MongoClient('mongodb://%s:%s/' % (self.host, self.port))[self.db_name]

    def get_collections(self):
        return self.connect().list_collection_names()

    def __select(self, collection_name):
        return self.connect()[collection_name]

    def get_all(self, collection_name):
        return self.__select(collection_name).find()

    def get_single(self, collection_name, dict_filter):
        return self.__select(collection_name).find_one(dict_filter)

    def search(self, collection_name, dict_filter):
        return self.__select(collection_name).find(dict_filter)

    def insert_entry(self, collection_name, dict_entry):
        return self.connect()[collection_name].insert_one(dict_entry).inserted_id

    def update_entry(self, collection_name, dict_filter, dict_new_entry):
        return self.connect()[collection_name].update_one(dict_filter, {'$set': dict_new_entry}).modified_count

    def delete(self, collection_name, dict_filter):
        return self.connect()[collection_name].delete_one(dict_filter).deleted_count
