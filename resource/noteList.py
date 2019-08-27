from flask import Flask
from flask_restful import Api, Resource, reqparse
from mongo import NoteDao
import datetime


class NoteList(Resource):
    dao = NoteDao()
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('word', type=str)
        args = parser.parse_args()
        word = args['word']
        if word == '':
            return self.dao.find_many(10)
        else : 
            return self.dao.find_by_word(word)

    
    

