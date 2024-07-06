from sqlite3 import Connection


class Database:
    """Абстрактный класс необходимый для создания интерфейсов взаимодействия с различными участниками базы данных"""
    _database: Connection

    def __init__(self, database: Connection) -> None:
        self._database = database
