from peewee import *

database = MySQLDatabase('video', **{'host': 'localhost', 'user': 'video', 'use_unicode': True, 'passwd': 'video', 'charset': 'utf8', 'port': 3306})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    head_img_url = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    nickname = CharField(constraints=[SQL("DEFAULT ''")])
    openid = CharField(index=True)

    class Meta:
        table_name = 'user'

