from Database.users import users, waiting_users, User
from constants import X, O


def pair_users(id1: int, id2: int):
    user1 = users[id1]
    user2 = users[id2]
    waiting_users.remove(id2)

    user1.opponent = user2.id
    user2.opponent = user1.id

    users[user1.id] = user1
    users[user2.id] = user2
    return user1, user2


def prepare_for_game(user1: User, user2: User):
    user1.create_desk()
    user2.create_desk()
    user1.shape = X
    user2.shape = O
    user1.move = True
    user2.move = False
    user1.games += 1
    user2.games += 1
