from sqlite3 import connect, Connection


class Database:
    """Абстрактный класс необходимый для создания интерфейсов взаимодействия с различными участниками базы данных"""
    _database: Connection

    def __init__(self, way_to_database) -> None:
        self._database = connect(way_to_database)

