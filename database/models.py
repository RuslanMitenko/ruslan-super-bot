from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('history.db')


class ModelBase(pw.Model):
    id = pw.AutoField()
    create_at = pw.DateField(default=datetime.now())

    class Meta:
        database = db


class History(ModelBase):
    message = pw.TextField()
