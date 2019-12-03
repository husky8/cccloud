import pymysql

def executesql(sql):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        database="cccloud",
        password="chenhongye1314.",
        charset="utf8")
    cursor = conn.cursor()
    sql = sql
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()