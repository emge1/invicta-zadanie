import requests
import sqlite3


def get_data(url):
    return requests.get(url).json()


users_url = 'https://jsonplaceholder.typicode.com/users'
todos_url = 'https://jsonplaceholder.typicode.com/todos'


def get_keys(obj, prev_key=None, keys=None):
    if keys is None:
        keys = []
    if type(obj) is not dict:
        keys.append(prev_key)
        return keys
    new_keys = []
    for x, y in obj.items():
        if prev_key is not None:
            new_key = "{}_{}".format(prev_key, x)
        else:
            new_key = x
        new_keys.extend(get_keys(y, new_key, []))
    return new_keys


def get_keys_types(keys, table):
    keys_types = {}
    for i in range(0, len(keys)):
        n = keys[i].split("_")
        if len(n) == 1:
            if type(table[0][keys[i]]) is str:
                keys_types[keys[i]] = "TEXT"
            elif type(table[0][keys[i]]) is int:
                keys_types[keys[i]] = "INT"
            elif type(table[0][keys[i]]) is bool:
                keys_types[keys[i]] = "NUMERIC"
        if len(n) == 2:
            if type(table[0][n[0]][n[1]]) is str:
                keys_types[keys[i]] = "TEXT"
        if len(n) == 3:
            if type(table[0][n[0]][n[1]][n[2]]) is str:
                keys_types[keys[i]] = "TEXT"
            elif type(table[0][n[0]][n[1]][n[2]]) is int:
                keys_types[keys[i]] = "INT"
    return keys_types


def create_table(tablename, keys_types):
    con = sqlite3.connect('../app/database.db')
    cur = con.cursor()
    req = f'''CREATE TABLE {tablename} ('''
    keys = list(keys_types.keys())
    for i in range(0, len(keys)):
        if i == 0:
            if tablename == "users":
                x = f'{keys[i]} {keys_types[keys[i]]} PRIMARY KEY, '
            else:
                x = f'{keys[i]} {keys_types[keys[i]]}, '
            req = req + x
        elif i != len(keys) - 1:
            if tablename == "todos" and i == 1:
                x = f'{keys[i]} {keys_types[keys[i]]} PRIMARY KEY, '
            else:
                x = f'{keys[i]} {keys_types[keys[i]]}, '
            req = req + x
        else:
            x = f'{keys[i]} {keys_types[keys[i]]})'
            req = req + x
    cur.execute(req)
    cur.close()


def save_data_sqlite(keys, table, tablename):
    reqs = []
    req_init = f"INSERT INTO {tablename} VALUES"
    req = req_init

    for i in range(0, len(table)):
        for k in range(0, len(keys)):
            n = keys[k].split("_")
            if k == 0:
                if len(n) == 1:
                    if type(table[i][n[0]]) == int:
                        req = req + f"({table[i][n[0]]}, "
                    else:
                        req = req + f"('{table[i][n[0]]}', "
                elif len(n) == 2:
                    req = req + f"('{table[i][n[0]][n[1]]}', "
                elif len(n) == 2:
                    req = req + f"('{table[i][n[0]][n[1]][n[2]]}', "

            elif k == len(keys) - 1:
                if len(n) == 1:
                    req = req + f"'{table[i][n[0]]}');"
                elif len(n) == 2:
                    req = req + f"'{table[i][n[0]][n[1]]}');"
                elif len(n) == 3:
                    req = req + f"'{table[i][n[0]][n[1]][n[2]]}');"

            else:
                if len(n) == 1:
                    if type(table[i][n[0]]) == bool:
                        req = req + f"({int(table[i][n[0]])}, "
                    else:
                        req = req + f"'{table[i][n[0]]}', "
                elif len(n) == 2:
                    req = req + f"'{table[i][n[0]][n[1]]}', "
                elif len(n) == 3:
                    req = req + f"'{table[i][n[0]][n[1]][n[2]]}', "

        reqs.append(req)
        con = sqlite3.connect('../app/database.db')
        cur = con.cursor()
        cur.execute(req)
        con.commit()
        req = req_init
    return reqs


if __name__ == '__main__':
    users = get_data(users_url)
    todos = get_data(todos_url)
    users_keys = get_keys(users[0])
    todos_keys = get_keys(todos[0])
    users_keys_types = get_keys_types(users_keys, users)
    todos_keys_types = get_keys_types(todos_keys, todos)
    create_table('users', users_keys_types)
    create_table('todos', todos_keys_types)
    save_data_sqlite(users_keys, users, "users")
    save_data_sqlite(todos_keys, todos, "todos")