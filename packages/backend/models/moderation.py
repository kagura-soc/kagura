from piccolo.table import Table
from piccolo.columns import Text, Boolean

class KReport(Table):
    id = Text(unique=True)
    note_id = Text(default=None)
    user_id = Text(default=None)
    
    reason = Text()

    is_resolved = Boolean()