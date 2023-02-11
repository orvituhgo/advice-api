import pymysql
import requests

conexao = pymysql.connect(
        host='localhost',
        user='root',
        password=None,
        db='cadastro',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

with conexao.cursor as cursor:
    cursor.excute(INSERT INTO





cursor. close()
conexao.close()