from sqlite3 import connect, Connection


class Database:
    _database: Connection

    def __init__(self, way_to_database) -> None:
        self._database = connect(way_to_database)

    def __del__(self):
        self._database.commit()
