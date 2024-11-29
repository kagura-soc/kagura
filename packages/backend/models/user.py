from tortoise import fields, Tortoise, run_async
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    title = fields.TextField()
    body = fields.TextField()

    class Meta:
        table = 'articles'
