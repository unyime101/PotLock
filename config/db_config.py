import mysql.connector

def db_con():# connectiuon method, will be used all throuh proj
    return mysql.connector.connect( 
        host="127.0.0.1",
        user="root",
        password="@Glory2003",
        database="potlock"
        )