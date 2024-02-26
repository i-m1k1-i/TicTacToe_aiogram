from dataclasses import dataclass
from constants import FREE, X, O

"""
What should be in user database:
    id INT PRIMARY KEY
    username varchar
    shape varhcar: X or O
    opponent  INT: another user's id
    desk list[int]: desk's instance in array
    games INT: played games num
    wins INT: num of won games
    win_rate INT PERCENT: percentage of won games
"""


@dataclass
class User:
    id: int
    username: str | None
    desk: list[int] | None = None
    opponent: int | None = None  # opponent's id
    move: int  # 1 my move, 0 not
    shape: int  # 1 - X, 2 - O

    def create_desk(self):
        self.desk = [FREE for _ in range(9)]
        users[self.id] = self


users: dict[int, User] = {}
waiting_users: list[int] = []  # id's of waiting users


def give_shapes(user1: User, user2: User):
    user1.shape = X
    user2.shape = O
