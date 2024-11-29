from piccolo.table import Table
from piccolo.columns import Text

class KEmoji(Table):
    id = Text(unique=True)
    emoji_code = Text(null=True)
    image_url = Text(null=True)
    description = Text()
