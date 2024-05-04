
import os
import psycopg2
import psycopg2.extras as ext

#funcao
def run_sql(sql, values = None):

    #variaveis de controle
    conn = None
    results = []

    #conexao com o banco de dados
    try:
        conn = psycopg2.connect("host=localhost port=5432 dbname=dbapp user=postgres password=123")
        cur = conn.cursor(cursor_factory = ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DataBaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results