from Database.users import users, waiting_users


def pair_users(id1: int, id2: int):
    user1 = users[id1]
    user2 = users[id2]
    waiting_users.remove(id2)

    user1.opponent = user2.id
    user2.opponent = user1.id

    users[user1.id] = user1
    users[user2.id] = user2
    return user1, user2
