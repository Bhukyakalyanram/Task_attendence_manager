from pymongo import MongoClient
import json
import time

database_url = "mongodb+srv://kalyanrambhukya69_db_user:Ks012606@cluster0.b5b4wpp.mongodb.net/?appName=Cluster0"
mongo_client = MongoClient(database_url)


student_database = mongo_client["students"]

student_collection = student_database["pythoncollection"]


# with open("MOCK_DATA.json") as file:
#     data = json.load(file)
#     # print(data)

# student_collection.insert_many(data)


# Batch_size = 100
# for i in range(0, len(data), Batch_size):
#     Batch = data[i, Batch_size + 1]
#     student_collection.insert_many(Batch)
# time.sleep(1)


cusrsor = student_collection.find({"email": {"$regex": "scribd.com"}})
student_collection

for item in cusrsor:
    print(item)
