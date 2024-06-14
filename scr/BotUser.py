from discord import Member


class BotUser:
    """Класс необходим для хранения данных юзера бота"""
    discord_id: int
    permissions_level: int
    money: float
    discord: Member

    def __init__(self, discord_id: int, permissions_level: int, money: float, discord: Member) -> None:
        self.discord_id = discord_id
        self.permissions_level = permissions_level
        self.money = money
        self.discord = discord
