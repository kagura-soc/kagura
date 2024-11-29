from piccolo.table import Table
from piccolo.columns import ForeignKey, Text

class KReaction(Table):
    id = Text()
    user = ForeignKey("KUser", null=False)
    note = ForeignKey("KNote", null=False, related_name="reactions")
    emoji = ForeignKey("KEmoji", null=False)