#imports
from database.run_sql import run_sql
from classes.agendamento import Agendamento

# Função para consultar agendamento
def get_all():
    
    agendamentos = []
    sql = 'select * from webuser.tb_agendamentos'

    results = run_sql(sql)

    for row in results:
        agendamento = Agendamento(row['cod_atividade'],
                                  row['cod_membro'],
                                  row['id_agendamento'])
        agendamentos.append(agendamento)
    return agendamentos

# Função para retornar um agendamento com base em um id
def get_one(id):

    sql = 'select * from webuser.tb_agendamentos where id_agendamento = %s'
    value = [id]

    result = run_sql(sql, value)[0]

    if result is not None:
        agendamento = Agendamento(result['cod_atividade'],
                                  result['cod_membro'],
                                  result['id_agendamento'])
    return agendamento

# Função para inserir novo agendamento
def new(agendamento):
    
    sql = 'INSERT INTO webuser.TB_AGENDAMENTOS ( cod_atividade, cod_membro ) VALUES ( %s, %s) RETURNING *;'
    values = [agendamento.cod_atividade, agendamento.cod_membro]

    result = run_sql(sql, values)

    agendamento.id_agendamento = result[0]['id_agendamento']

# Função para deletar um agendmento com base no id
def delete_one(id):

    sql = 'delete from webuser.tb_agendamentos where id_agendamento = %s'
    value = [id]

    result = run_sql(sql, value)

# Função para verificar se um agendamento existe
def verifica_agendamento(atividade, membro):

    sql = 'select * from webuser.tb_agendamento where cod_atividade = %s and cod_membro = %s'
    values = [atividade, membro]

    results = run_sql(sql, values)

    if len(results) == 0:
        return False
    else:
        return True

# Função para deletar um agendamento com base no id e no membro
def delete_agendamento(membro, atividade):
    
    sql = "DELETE  FROM webuser.TB_AGENDAMENTOS WHERE cod_membro = %s and cod_atividade = %s"
    values = [membro, atividade]
    
    run_sql(sql, values)

