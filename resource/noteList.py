from flask import Flask
from flask_restful import Api, Resource, reqparse
from mongo import NoteDao
import datetime


class NoteList(Resource):
    dao = NoteDao()
    def get(self):
        result = self.dao.find_many(10)
        return result

    
    

