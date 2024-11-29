from piccolo.conf.apps import AppRegistry
from psqlpy_piccolo import PSQLPyEngine

from scripts.load_conf import load

config = load()

DB = PSQLPyEngine(
    config={
        "host": config.db.host,
        "port": config.db.port,
        "user": config.db.user,
        "password": config.db.password,
        "database": config.db.dbname,
    },
)

APP_REGISTRY = AppRegistry(apps=['piccolo_app'])
