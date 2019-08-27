from flask import Flask
from flask_restful import Api, Resource, reqparse
from mongo import NoteDao
import datetime

class ToNote(Resource):
    dao = NoteDao()

    def get(self):    
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        args = parser.parse_args()
        id = args['id']
        dictionary = self.dao.find_one(id)
        return dictionary

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('content', type=str)
        parser.add_argument('type', type=str)
        parser.add_argument('keyword', type=str)
        args = parser.parse_args()
        data = {
            "name" : args['name'],
            "content" : args['content'],
            "type" : args['type'],
            "keyword" : args['keyword'].split(','),
            "creating_time" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        id = self.dao.add(data)
        return {
                "info" : "A note has been created.",
                "_id" : id
                }, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        args = parser.parse_args()
        id = args['id']
        deleted_count = self.dao.delete_one(id)
        if deleted_count == 1:
            return {"info" : "A note has been deleted."}, 200
        elif deleted_count == 0:
            return {"info" : "note with id:["+id+"] does not exists."}, 200
        else:
            return {"info" : "Got no idea what happend."}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('_id', type=str)
        parser.add_argument('name', type=str)
        parser.add_argument('content', type=str)
        parser.add_argument('type', type=str)
        parser.add_argument('keyword', type=str)
        args = parser.parse_args()
        id = args['_id']
        data = {
            "name" : args['name'],
            "content" : args['content'],
            "keyword" : args['keyword'].split(','),
            "type" : args['type']
        }
        modified_count = self.dao.update_one(id, data)
        if modified_count == 1:
            return {"info" : "A note has been updated."}, 200
        elif modified_count == 0:
            return {"info" : "note with id:["+id+"] does not exists."}, 200
        else:
            return {"info" : "Got no idea what happend."}, 500
