import mysql.connector as mysql

def connect(dbname):
    try:
        return mysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = dbname
    )
    except Error as e:
        print(e)

if __name__ = '__main__':
    db = connect("projects")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    print(project_records)
    db.close()