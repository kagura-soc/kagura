from piccolo.table import Table
from piccolo.columns import ForeignKey, Text, Varchar

class KNote(Table):
    id = Text()
    user = ForeignKey("KUser", null=False)
    
    cw = Varchar(length=100)
    content = Varchar(length=3000)
    created_at = Text()

    media = ForeignKey("Media", null=True)
    reply = ForeignKey("KNote", null=True)
    original = ForeignKey("KNote", null=True)