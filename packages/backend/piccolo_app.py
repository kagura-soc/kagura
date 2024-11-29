import os

from piccolo.conf.apps import AppConfig
from models import (
    KFollows, 
    KEmoji, 
    KHost, 
    KNote, 
    KReaction, 
    KUser,
)


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name='kagura',
    migrations_folder_path=os.path.join(
        CURRENT_DIRECTORY,
        'migrations'
    ),
    table_classes=[KFollows, KEmoji, KHost, KNote, KReaction, KUser],
    migration_dependencies=[],
    commands=[]
)