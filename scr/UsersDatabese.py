from discord import Member

from scr.BotUser import BotUser
from scr.Database import Database


class UsersDatabase(Database):
    """Позволяет работать с таблицей users в базе данных"""

    def create_table(self) -> None:
        """Создаёт таблицу users в базе данных"""
        cursor = self._database.cursor()
        cursor.execute("""
            CREATE TABLE users (discord_id INTEGER, permissions_level INTEGER, money FLOAT);
        """)

    def check_user(self, author: Member) -> bool:
        """Проверяет наличие юзера в системе"""
        cursor = self._database.cursor()
        cursor.execute(f"""
                    SELECT * 
                    FROM users 
                    WHERE discord_id={author.id};
                """)
        if cursor.fetchone() is None:
            return False
        else:
            return True

    def get_user(self, author: Member) -> BotUser | None:
        """Достаёт юзера из базы данных"""
        cursor = self._database.cursor()
        cursor.execute(f"""
            SELECT * 
            FROM users 
            WHERE discord_id={author.id};
        """)
        user = BotUser(*cursor.fetchone(), discord=author)
        return user

    def add_user(self, author: Member) -> BotUser:
        """Добавляет нового юзера в базу данных"""
        cursor = self._database.cursor()
        user = BotUser(discord_id=author.id, permissions_level=1, money=0, discord=author)
        cursor.execute(f"""
            INSERT INTO users (discord_id, permissions_level, money) 
            values ({user.discord_id}, {user.permissions_level}, {user.money});
        """)
        self._database.commit()
        return user

    def edit_user_money(self, user: BotUser, value: float) -> None:
        """Изменяет количество денег у юзера"""
        cursor = self._database.cursor()
        cursor.execute(f"""
            UPDATE users 
            SET money={value}
            WHERE discord_id={user.discord_id};
        """)
        self._database.commit()
        user.money = value

    def edit_user_permission_level(self, user: BotUser, value: int) -> None:
        """Изменяет уровень прав юзера"""
        cursor = self._database.cursor()
        cursor.execute(f"""
                    UPDATE users 
                    SET permissions_level={value}
                    WHERE discord_id={user.discord_id};
                """)
        self._database.commit()
        user.permission = value
