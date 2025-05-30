from .db_config import db_con #correct file path allowing me to accces meth in db con

def get_tables():#Testing connection 
    con = db_con()
    cursor = con.cursor()
    cursor.execute("Show TABLES")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    con.close()
    