from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
database_url = "mongodb+srv://kalyanrambhukya69_db_user:Ks012606@cluster0.b5b4wpp.mongodb.net/?appName=Cluster0"
mongoclient = MongoClient(database_url)
student_database = mongoclient["students"]
student_collection = student_database["pythoncollection"]


@app.get("/search")
def handle_get_data():
    searchkey = request.args.get("data")
    cursor = student_collection.find({"first_name": {"$regex": searchkey}})

    students = list(cursor)

    students = list(map(lambda x: {**x, "_id": str(x["_id"])}, students))

    return students


if __name__ == "__main__":
    app.run(debug=True)
