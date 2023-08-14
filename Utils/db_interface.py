import sqlite3
import os
from sqlite3 import Error


db_name = f'{os.path.dirname(os.getcwd())}\\MajorLeagueDiscordball\\mld.db'
SYMBOL = '?'


def create_connection(db_file):
    this_connection = None
    try:
        this_connection = sqlite3.connect(db_file, isolation_level=None)
    except Error as e:
        print(e)
    return this_connection


def fetch_all(sql_query, data):
    try:
        this_connection = get_connection()
        cursor = this_connection.cursor()
        cursor.execute(sql_query, data)
        return cursor.fetchall()
    except Error as e:
        print(e)


def fetch_one(sql, data):
    try:
        this_connection = get_connection()
        cursor = this_connection.cursor()
        cursor.execute(sql, data)
        return cursor.fetchone()
    except Error as e:
        print(e)


def update_database(sql, data):
    try:
        this_connection = get_connection()
        cursor = this_connection.cursor()
        cursor.execute(sql, data)
        this_connection.commit()
    except Error as e:
        print(e)


def update_table(table_name: str, columns: dict, where: dict):
    sql = f'''UPDATE {table_name} SET'''
    data = []
    for item in columns:
        sql += f' {item}={SYMBOL},'
        data.append(columns[item])
    sql = sql[0:-1]
    sql += ' WHERE'
    for condition in where:
        if where[condition] is not None:
            sql += f' {condition}={SYMBOL} AND'
            data.append(where[condition])
        else:
            sql += f' {condition} IS NULL AND'
    sql = sql[0:-4]  # trim extra AND at the end
    update_database(sql, tuple(data))


def select_data(table_name: str, columns: str, conditions: dict):
    sql = f'''SELECT {columns} FROM {table_name}'''
    data = []
    if conditions:
        sql += ' WHERE'
        for item in conditions:
            if conditions[item] is not None:
                sql += f' {item}={SYMBOL} AND'
                data.append(conditions[item])
            else:
                sql += f' {item} IS NULL AND'
        sql = sql[0:-4]
    return fetch_all(sql, tuple(data))


def insert_data(table_name: str, attributes: dict):
    columns = ''
    values = ''
    data = []
    for item in attributes:
        columns += f'{item}, '
        values += '?,'
        data.append(attributes[item])
    columns = columns[0: -2]  # trim extra , at the end
    values = values[0:-1]
    sql = f'''INSERT INTO {table_name} ({columns}) VALUES ({values})'''
    update_database(sql, tuple(data))


def get_connection():
    if connection:
        return connection
    else:
        return create_connection(db_name)


connection = create_connection(db_name)
