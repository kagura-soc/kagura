from piccolo.conf.apps import AppRegistry
try:
    from psqlpy_piccolo import PSQLPyEngine
except ModuleNotFoundError as e:
    from piccolo.engine.postgres import PostgresEngine
    PSQLPyEngine = None

from scripts.load_conf import load

config = load()
db_config = {
    "host": config.db.host,
    "port": config.db.port,
    "user": config.db.user,
    "password": config.db.password,
    "database": config.db.dbname,
}

if PSQLPyEngine:
    DB = PSQLPyEngine(config=db_config)
else:
    DB = PostgresEngine(config=db_config)

APP_REGISTRY = AppRegistry(apps=['piccolo_app'])
