# from mongodb_utility import MongoUtility
#
# for item in MongoUtility('localhost', 27017, 'my_db').get_collections():
#     print(item)
from collections import namedtuple


class Employee:
    def __int__(self):
        self.age = 0
        self.name = ''

d = {'afawf':'444', 'age': 20, 'name': 'joe'}


aaa = namedtuple("Employee", d.keys())(*d.values())
print(aaa)



db = MongoUtility('localhost', 27017, 'my_db')
db2 = MongoUtility('localhost', 27017, 'awfwfw')
print(db.connect().list_collection_names())
print(db2.connect().list_collection_names())