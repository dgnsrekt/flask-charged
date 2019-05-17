from peewee import SqliteDatabase
from peewee import Model, CharField, BigIntegerField, BlobField, DateTimeField, DecimalField

DATABASE = SqliteDatabase("example.db")


class Invoice(Model):

    r_hash = BlobField(unique=True)
    r_hash_string = CharField(unique=True)
    payment_request = CharField(unique=True)
    satoshi_amount = BigIntegerField()
    description = CharField(null=True)
    add_index = BigIntegerField(unique=True)
    # created_at = DateTimeField()
    # expires_at = DateTimeField()

    class Meta:
        database = DATABASE
