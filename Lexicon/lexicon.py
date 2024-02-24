class Lexicon:
    start: str = "В этом боте ты можешь сыграть в различные игры с другими пользователями"
    main_menu = "Главное меню"
    searching_opponent: str = "Ищем противника..."

    def get_user_profile(self, username: str | None, user_id: int):
        return f"""My profile:
        username: {username}
        id: <code>{user_id}</code>"""


lexicon_ru = Lexicon()


menu = (("Играть в ХО", "playXO"), ("Профиль", "profile"))
