import discord

from main import sdb
from scr import phrases_func
from scr.SportDatabase import SportDatabase

from scr.cfg import sport_phrases


def get_exersice_four_select(database: SportDatabase) -> list:
    exersice = database.get_exercises()
    for row in range(len(exersice)):
        exersice[row] = discord.SelectOption(label=str(exersice[row][0]))
    return exersice


class SportMenu(discord.ui.View):
    def __init__(self):
        super().__init__(
            timeout=None
        )

    @discord.ui.button(
        label="Профиль",
        style=discord.ButtonStyle.blurple
    )
    async def profile(self, interaction: discord.Interaction, button: discord.ui.Button):

        # тут нужно подготовить вид профиля

        # embed = discord.Embed(colour=discord.Colour.random()).set_author(name=f"{interaction.user.mention}")
        await interaction.response.send_message("123")

    @discord.ui.button(
        label="Дневник",
        style=discord.ButtonStyle.green
    )
    async def diary(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="Выбери упражнение, повтор котого хочешь записать.", view=SelectExersice())

    @discord.ui.button(
        label="Выйти",
        style=discord.ButtonStyle.danger
    )
    async def exit(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.stop()
        await interaction.response.edit_message(
            content=str_func.random_phrase(sport_phrases.end_of_train_phrases),
            view=None,
            embed=None,
            delete_after=2.0
        )


class SelectExersice(discord.ui.View):
    def __init__(self):
        super().__init__(
            timeout=None
        )

    @discord.ui.select(
        placeholder="Выбери упражнение",
        min_values=1,
        max_values=1,
        options=get_exersice_four_select(sdb)
    )
    async def select_channels(self, interaction: discord.Interaction, select: discord.ui.Select):
        modal = RepeatsForm(title=select.values[0])
        await interaction.response.send_modal(modal)


class RepeatsForm(discord.ui.Modal):
    count_exersice = discord.ui.TextInput(label="Введи кол-во повторений:")

    def __init__(self, title: str):
        super().__init__(
            timeout=None,
            title=title
        )

    async def on_submit(self, interaction: discord.Interaction):
        # прописать добавление нового подхода в базу
        embed = discord.Embed(
            title="Подход успешно добавлен.",
            color=discord.Color.random()
        ).add_field(
            name=f"{self.title}:",
            value=f"{self.count_exersice.value} раз",
        )

        await interaction.response.edit_message(
            content=f"SPORT MENU\n{str_func.random_phrase(sport_phrases.sport_greeting_phrases)}",
            embed=embed,
            view=SportMenu()
        )
