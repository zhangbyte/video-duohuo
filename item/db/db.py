from peewee import *

database = MySQLDatabase('video', **{'host': 'localhost', 'user': 'video', 'use_unicode': True, 'passwd': 'video', 'charset': 'utf8', 'port': 3306})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Item(BaseModel):
    click = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    text = CharField()
    user_id = BigIntegerField(column_name='user_id')
    video = CharField()

    class Meta:
        table_name = 'item'

