from classes.plano import TipoPlano
from database.run_sql import run_sql

#funcao para obter todos os planos
def get_all():
    
    tipos_planos = []

    sql = 'select * from webuser.tb_planos'
    results = run_sql(sql)
    
    for row in results:
        tipo_plano = TipoPlano(row['plano'], row['id_plano'])
        tipos_planos.append(tipo_plano)

    return tipos_planos

#funcao para pegar apenas um plano
def get_one(id):
    
    sql = 'select * from webuser.tb_planos where id_plano = %s'
    value = [id]

    result = run_sql(sql, value)[0]

    if result is not None:
        tipo_plano = TipoPlano(result['plano'], result['id_plano'])

    return tipo_plano

#funcao para criar um plano
def new(tipo_plano):
    
    sql = 'insert into webuser.tb_planos (plano) values (%s) RETURNING *;'
    values = [tipo_plano.plano]

    results = run_sql(sql, values)  

    tipo_plano.id_plano = results[0]['id_plano']
    
    return tipo_plano

#funcao para deletar um plano
def delete_one(id):

    sql = 'delete from webuser.tb_planos where id_plano = %s'
    value = [id]

    run_sql(sql, value)

#funcao para alterar um plano
def edit(tipo_plano):

    sql= "update webuser.tb_planos set (plano) = (%s) where id_plano = %s;"
    values = [tipo_plano.plano, tipo_plano.id_plano]

