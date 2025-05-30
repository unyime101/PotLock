import mysql.connector

def db_con():# connectiuon method, will be used all throuh proj
    return mysql.connector.connect( 
        host="localhost",
        user="root",
        password="@Glory2003",
        database="PotLock"
        )