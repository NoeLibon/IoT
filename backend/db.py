#mongosh "mongodb://data-shard-00-00.jlxea.mongodb.net:27017,data-shard-00-01.jlxea.mongodb.net:27017,data-shard-00-02.jlxea.mongodb.net:27017/data?replicaSet=atlas-yejunu-shard-0" --ssl --authenticationDatabase admin --username noe --password user123

import pymongo

class Storage:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://noe:user123@data.jlxea.mongodb.net/data?retryWrites=true&w=majority")
        self.db = self.client["data"]
        self.col = self.db["customers"]

        self.list = [
            {"name": "Amy", "address": "Apple st 652"},
            {"name": "Hannah", "address": "Mountain 21"},
            {"name": "Michael", "address": "Valley 345"},
            {"name": "Sandy", "address": "Ocean blvd 2"},
            {"name": "Betty", "address": "Green Grass 1"},
            {"name": "Richard", "address": "Sky st 331"},
            {"name": "Susan", "address": "One way 98"},
            {"name": "Vicky", "address": "Yellow Garden 2"},
            {"name": "Ben", "address": "Park Lane 38"},
            {"name": "William", "address": "Central st 954"},
            {"name": "Chuck", "address": "Main Road 989"},
            {"name": "Viola", "address": "Sideway 1633"}
        ]

        self.col.insert_many(self.list)

    def print_data(self):
        print(self.col)


if __name__ == '__main__':
    s = Storage()
    s.print_data()
