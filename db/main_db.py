import sqlite3
from config import path_db
from db import queries
from datetime import datetime

# a = ()
# b = []
# c = {}

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.create_tasks_table)
    print('data base COOOnected!!@!@')
    conn.commit()
    conn.close()


# def add_task(task):
#     conn = sqlite3.connect(path_db)
#     cursor = conn.cursor()
#     # cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task, ))
#     cursor.execute(queries.insert_task, (task,))
#     conn.commit()
#     task_id = cursor.lastrowid
#     conn.close()
#     return task_id

def add_task(task):
    date = datetime.now().strftime("%Y/%m/%d - %h:%m")
    with sqlite3.connect(path_db) as conn: 
        cursor = conn.cursor()
        cursor.execute(queries.insert_task, (task, date))
        task_id = cursor.lastrowid
    return task_id, date


def update_task(task_id, new_task=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if new_task is not None:
        cursor.execute(queries.update_task, (new_task, task_id))
    
    conn.commit()
    conn.close()
