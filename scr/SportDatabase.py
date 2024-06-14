from datetime import datetime
import pickle

from scr.Database import Database
from scr.BotUser import BotUser


class SportDatabase(Database):

    def create_table_exercises(self) -> None:
        cursor = self._database.cursor() # таблицу repeats необходимо содать в базе
        cursor.execute("""
            CREATE TABLE exercises ("name" STRING, "type" STRING);
            CREATE TABLE repeats ( 
                "discord_id" INTEGER, 
                "exercises_type" INTEGER, 
                "count" INTEGER, 
                "datetime" BYTES, 
            );
        """)

    def get_exercises(self) -> list[str]:
        cursor = self._database.cursor()
        cursor.execute("""
            SELECT * FROM exercises;
        """)
        return cursor.fetchall()

    def add_exersice(self, exersice: str) -> None:
        cursor = self._database.cursor()
        cursor.execute(f"""
            INSERT INTO exercises (name)
            values ('{exersice}');
        """)
        self._database.commit()

    def get_repeats(self,
                    user: BotUser | None = None,
                    exersice_type: str | None = None,
                    count: int | None = None,
                    datatime: datetime | None = None) -> list:
        pass # тут сделать выборку в соответствии с тем, какой фильтр был указан при вызове функции

    def add_repeats(self,
                    user: BotUser,
                    exersice_type: str,
                    count: int,
                    datatime: datetime) -> None:
        pass # тут сделать сериализацию datetime picle
