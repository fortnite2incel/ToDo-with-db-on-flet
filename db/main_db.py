import sqlite3
from config import path_db
from datetime import datetime
from db.queries import *

# a = ()
# b = []
# c = {}

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(create_tasks_table)
    existing = [row[1] for row in cursor.execute("PRAGMA table_info(tasks)").fetchall()]
    if 'date' not in existing:
        cursor.execute("ALTER TABLE tasks ADD COLUMN date TEXT")

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
        cursor.execute(insert_task, (task, date)) 
        task_id = cursor.lastrowid
    return task_id, date


def update_task(task_id, new_task=None, completed=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if new_task is not None:
        cursor.execute(update_task_query, (new_task, task_id))
    elif completed is not None:
        cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (completed, task_id))
    
    conn.commit()
    conn.close()


def get_tasks(filter_type='all'):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if filter_type == 'completed':
        cursor.execute(select_tasks_completed)
    elif filter_type == 'uncompleted':
        cursor.execute(select_tasks_uncompleted)
    else:
        cursor.execute(select_tasks)
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def clear_completed():
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(delete_completed_tasks)
        conn.commit()
 
 
def delete_task_by_id(task_id):
    with sqlite3.connect(path_db) as conn:
        cursor = conn.cursor()
        cursor.execute(delete_task, (task_id,))
        conn.commit()
