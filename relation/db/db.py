from peewee import *

database = MySQLDatabase('video', **{'host': 'localhost', 'user': 'video', 'use_unicode': True, 'passwd': 'video', 'charset': 'utf8', 'port': 3306})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Love(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    from_user_id = BigIntegerField(column_name='from_user_id')
    id = BigAutoField()
    item_id = BigIntegerField(column_name='item_id')

    class Meta:
        table_name = 'love'

class Relation(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    from_user_id = BigIntegerField(column_name='from_user_id')
    id = BigAutoField()
    to_user_id = BigIntegerField(column_name='to_user_id')

    class Meta:
        table_name = 'relation'
