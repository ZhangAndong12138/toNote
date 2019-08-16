from flask_restful import Resource
from database import Mysql

class HelloWorld(Resource):
    def get(self, note_id):
        return {
            "why not": "take a note",
            "note_id": note_id
            }



        # mysql = Mysql(None)
        # mysql.connect()
        # sql = "insert into note (name, content, type, keyword, create_time, update_time) \
        #     values ('IDEA 去处无效引用快捷键', 'Alt + Ctrl + O', 'intellij IDEA', 'IDEA 快捷键', now(), now())"
        # mysql.execute_sql(sql)
        # mysql.disconnect()
