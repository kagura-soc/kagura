from piccolo.table import Table
from piccolo.columns import ForeignKey, Text

class KNote(Table):
    id = Text()
    user = ForeignKey("KUser", null=False)
    
    content = Text()
    created_at = Text()