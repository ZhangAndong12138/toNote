import pymongo
from bson.objectid import ObjectId

class NoteDao(object):
    client = pymongo.MongoClient("mongodb://47.93.23.130:27017/")
    db = client["toNote"]
    col = db["note"]
    collection = col

    def find_one(self, id):
        """查找一个Note"""
        dictionary = self.collection.find_one({"_id" : ObjectId(id)})
        dictionary["_id"] = str(dictionary["_id"])
        return dictionary

    def find_many(self, num):
        """查找多个Note num为数量 默认排序"""
        cursor = self.collection.find().limit(num)
        result = []
        for dictionary in cursor:
            dictionary["_id"] = str(dictionary["_id"])
            result.append(dictionary)
        return result
       
    def add(self, data):
        """新增一个Note"""
        return str(self.collection.insert(data))

    def delete_one(self, id):
        """按指定id删除一个Note"""
        return self.collection.delete_one({"_id" : ObjectId(id)}).deleted_count

    def update_one(self, id, data):
        """更新指定id的Note"""
        return self.collection.update_one({"_id" : ObjectId(id)}, {"$set": data}).modified_count

    def find_by_word(self, word):
        """按关键字模糊查询"""
        print(word)
        query = {"name": {"$regex" : word }}
        cursor = self.collection.find(query)
        result = []
        for dictionary in cursor:
            dictionary["_id"] = str(dictionary["_id"])
            result.append(dictionary)
        return result



