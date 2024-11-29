from piccolo.table import Table
from piccolo.columns import Text, ForeignKey

class KMedia(Table):
    id = Text()
    filename = Text()
    
    path = Text(default=None)
    url = Text(default=None)
    
    filesize = Text()
    
    owner = ForeignKey(references="KUser", null=True, related_name="media")
    notes = ForeignKey(references="KNote", null=True, related_name="media")