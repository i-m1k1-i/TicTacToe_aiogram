from Database.users import User


class Lexicon:
    start: str = "В этом боте ты можешь сыграть в различные игры с другими пользователями"
    main_menu: str = "Главное меню"
    searching_opponent: str = "Ищем противника..."
    you_win: str = "Поздравляю, Вы победили!"
    you_lose: str = "К сожелению вы проиграли, повезет в следующий раз."
    its_tie: str = "Это ничья, вы были равными соперниками."

    def get_user_profile(self, user: User):
        return f"""Профиль:
        username: {user.username}
        id: <code>{user.id}</code>
        Игр сыграно: {user.games}
        Игр выиграно: {user.wins}
        Процент побед: {user.get_win_rate()}%
        """


lexicon_ru = Lexicon()


menu = [("Играть в ХО", "playXO"), ("Профиль", "profile")]
