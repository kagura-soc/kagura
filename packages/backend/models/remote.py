from piccolo.table import Table
from piccolo.columns import UUID, Text, ForeignKey,Boolean

class KHost(Table):
    id = UUID()
    host = Text()
    users = ForeignKey("KUser")
    
    webfinger = Text()
    inbox = Text()
    nodeinfo = Text()
    
    is_suspended = Boolean(default=False)
    is_blocked = Boolean(default=False)
    is_muted = Boolean(default=False)