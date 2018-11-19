import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['dtvthetest']
mycollect = mydb['dtvthetestcollect']
# print(mycollect)
#
# print(myclient.list_database_names())
# print(mydb.list_collection_names())

my_data_insert_one = {'name': 'Harry Smith', 'address': 'Downtown - LA'}
my_data_insert_many = [
    {'name': 'Jayce Kenne', 'address': 'W.DC - LA'},
    {'name': 'Piter Azk', 'address': 'Newyork'},
    {'name': 'Marry PiPin', 'address': 'Missispi'}
]
# x = mycollect.insert_one(my_data_insert_one)
# print(x.inserted_id)

# x = mycollect.insert_many(my_data_insert_many)
# # print(x.inserted_ids)

# x = mycollect.find_one()
# print(x)

# x = mycollect.find()
# for a in x:
#     print(a)


# x = mycollect.find({}, {'_id':1})
# # for a in x:
# #     print(a)

# query = {'name': 'Piter Azk'}
# x = mycollect.find(query)
# for a in x:
#     print(a)

# x = mycollect.find().limit(2)
# for a in x:
#     print(a)

# my_query = {'address':{'$regex':'.*LA'}}
# x = mycollect.find(my_query)
# for a in x:
#     print(a)

# x = mycollect.find().sort('name', -1)
# for a in x:
#     print(a)


my_query_old_value = {'address': 'Newyork'}
my_query_new_value = {'$set': {'address': 'Viet Nam'}}
mycollect.update_one(my_query_old_value, my_query_new_value)
