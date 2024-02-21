from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    desk: list[list[int]] | None = None
    opponent: int | None = None  # opponent's id


users: dict[int, User] = {}
waiting_users: list[int] = []  # id's of waiting users
