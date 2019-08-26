from flask import Flask
from flask_restful import Api, Resource
from flask_cors import *
from resource.note import ToNote
from resource.noteList import NoteList
from database import Mysql

app = Flask(__name__)
CORS(app)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
api = Api(app)
api.add_resource(NoteList, '/')
api.add_resource(ToNote, '/notes')

if __name__ == '__main__':
    app.run(debug=True)