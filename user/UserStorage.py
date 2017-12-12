import json

import os

from user.User import User

USERS_FILE = 'users.json'


def read_all_users():
    result = []
    if os.stat(USERS_FILE).st_size > 0:
        events = open(USERS_FILE, 'r')
        json_loads = json.load(events)
        for json_load in json_loads:
            event = User(None, None)
            event.__dict__.update(json_load)
            result.append(event)
        events.close()
    return result


def save_users(users):
    dumps_list = []
    for user in users:
        dumps_list.append(user.__dict__)
    users_file = open(USERS_FILE, 'w')
    json.dump(dumps_list, users_file)
    users_file.close()


def save_user(user):
    all_users = read_all_users()
    all_users.append(user)
    save_users(all_users)
