import pymongo
from bson.objectid import ObjectId

class NoteDao(object):
    client = pymongo.MongoClient("mongodb://47.93.23.130:27017/")
    db = client["toNote"]
    col = db["note"]
    collection = col

    def find_one(self, id):
        """查找一个"""
        dictionary = self.collection.find_one({"_id" : ObjectId(id)})
        dictionary["_id"] = str(dictionary["_id"])
        return dictionary

    def find_many(self, num):
        """查找多个 num为数量"""
        cursor = self.collection.find().limit(num)
        result = []
        for dictionary in cursor:
            dictionary["_id"] = str(dictionary["_id"])
            result.append(dictionary)
        return result
       
    def add(self, data):
        return str(self.collection.insert(data))

    def delete_one(self, id):
        return self.collection.delete_one({"_id" : ObjectId(id)}).deleted_count

