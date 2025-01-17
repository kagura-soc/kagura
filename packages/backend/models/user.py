from piccolo.table import Table
from piccolo.columns import ForeignKey, Varchar, Text, UUID, Boolean

class KFollows(Table):
    id = UUID()
    followee = ForeignKey("KUser", null=False)
    follower = ForeignKey("KUser", null=False)

class KIPLog(Table):
    id = UUID()
    user = ForeignKey("KUser", null=False)
    ip_address = Text()

class KUser(Table):
    id = Text()
    handle = Varchar(length=256, unique=True, null=False) # TODO: ^[a-zA-Z0-9_]+$にあわないハンドルを弾く
    display_name = Varchar(length=256)
    
    email = Text(unique=True, null=True) # TODO: バックエンド側で^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$に合わない場合は弾く
    password = Text()
    totp_seed = Text()
    
    followers = ForeignKey("KFollows", related_name="followee")
    following = ForeignKey("KFollows", related_name="follower")
    
    notes = ForeignKey("KNote", related_name="user")
    reactions = ForeignKey("KReaction", related_name="user")
    
    public_key = Text() 
    private_key = Text(default=None)
    
    host = ForeignKey("KHost", default=None)
    
    is_suspended = Boolean()
    is_muted = Boolean()