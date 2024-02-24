import sqlite3
from sqlite3 import connect


class User:
    __discord_id: int
    __money: int
    __permission_level: int
    __db: Database

    def __init__(self, user_discord_id: int, user_money: int, user_permission_level: int, database: Database) -> None:
        self.__discord_id = user_discord_id
        self.__money = user_money
        self.__permission_level = user_permission_level
        self.__db = database


class Database:
    __db: sqlite3.Connection
    __cursor: sqlite3.Cursor

    def __init__(self, way_to_database: str) -> None:
        self.__db = connect(way_to_database)
        self.__cursor = self.__db.cursor()

    def create_tables(self) -> None:
        """Создаёт новую, чистую таблицу users.
        users: (discord_id, money, permission_level)
        """
        self.__cursor.execute(__sql="CREATE TABLE users (discord_id INTEGER, money INTEGER, permission_level INTEGER)")

    def get_user(self, user_discord_id: int) -> User | None:
        """Возвращает коллекцию данных пользователя.
        user[0] - user_discord_id
        user[1] - user_money
        user[2] - user_permission_level
        """
        user = self.__cursor.execute(__sql=f"SELECT * FROM users WHERE discord_id = {user_discord_id}").fetchone()
        if user is None:
            return None
        else:
            return User(*user, self)

    def add_user(self, user_discord_id: int) -> None:
        """Добавляет в базу нового пользователя."""
        self.__cursor.execute(__sql=f"INSERT INTO users VALUES ({user_discord_id}, 0, 1)")


