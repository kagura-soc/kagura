import os

from piccolo.conf.apps import AppConfig
import models


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name='kagura',
    migrations_folder_path=os.path.join(
        CURRENT_DIRECTORY,
        'migrations'
    ),
    table_classes=models.__all__,
    migration_dependencies=[],
    commands=[]
)