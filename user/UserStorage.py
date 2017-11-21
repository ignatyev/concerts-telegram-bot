from user.User import User


def save_user(user_id):
    print('saving user: ' + str(user_id))
    users = open('users.txt', 'a')
    users.write(str(user_id))
    users.write('\n')
    users.close()


def read_all_users():
    result = []
    users = open('users.txt', 'r')
    for user_id in users.readlines():
        result.append(User(user_id))
    users.close()
    return result
