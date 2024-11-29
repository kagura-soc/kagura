from tortoise import fields, Tortoise, run_async
from tortoise.models import Model

class Note(Model):
    id = fields.TextField()
    cw = fields.TextField()
    body = fields.TextField()

    class Meta:
        table = 'notes'
