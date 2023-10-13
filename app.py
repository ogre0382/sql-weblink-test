import streamlit as st
import sqlite3
import pandas as pd

# データベースに接続する
conn = sqlite3.connect('example.db')
c = conn.cursor()

# データを表示する
def show_data():
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    for d in data:
        st.write(d)
        st.link_button(d[3],d[2])

def show_table():
    df_from_sql2 = pd.read_sql('SELECT * FROM users', conn)
    #st.dataframe(df_from_sql2)
    st.write(df_from_sql2)

# データを追加する
def add_data(name, link ,title):
    c.execute('INSERT INTO users (Name, Link, Title) VALUES (?, ?, ?)', (name, link, title))
    conn.commit()
    st.write('Data added. Please reload page.')

# データベースにテーブルを作成する
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Link TEXT, Title TEXT)')

# データの表示
show_data()
show_table()

# データの追加
name = st.text_input('Name')
link = st.text_input('Link')
title = st.text_input('Title')
if st.button('Add data'):
    add_data(name, link, title)

# データベースをクローズする
conn.close()
