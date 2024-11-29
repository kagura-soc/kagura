from piccolo.table import Table
from piccolo.columns import ForeignKey, Text, Varchar, Date

class KNote(Table):
    id = Text()
    user = ForeignKey("KUser", null=False)
    
    cw = Varchar(length=100)
    content = Varchar(length=3000)
    created_at = Date()

    media = ForeignKey("Media", null=True)
    reply = ForeignKey("KNote", null=True)
    original = ForeignKey("KNote", null=True)