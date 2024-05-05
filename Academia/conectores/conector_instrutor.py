from database.run_sql import run_sql
from classes.instrutor import Instrutor
from classes.atividade import Atividade

#funcao para listar todos os instrutores
def get_all():
    instrutores = []

    sql = 'select * from webuser.tb_intrutores'
    results = run_sql(sql)

    for row in results:

        instrutor = Instrutor(row['nome'],
                              row['sobrenome'],
                              row['data_nascimento'],
                              row['endereco'],
                              row['telefone'],
                              row['id_instrutor'])
        
        instrutores.append(instrutor)
    return instrutores

#funcao para retornar um instrutor
def get_one(id):

    sql = 'select * from webuser.tb_intrutores where id_instrutor = %s'
    value = [id]

    result = run_sql(sql, value)[0]

    if result is not None:
        instrutor = Instrutor(result['nome'],
                              result['sobrenome'],
                              result['data_nascimento'],
                              result['endereco'],
                              result['telefone'],
                              result['id_instrutor'])
    return instrutor

#funcao para listar todas as atividades de um instrutor
def get_activities(instructor_id):

    atividades = []

    sql = "select * from webuser.tb_atividades where cod_instrutor = %s"
    values = [instructor_id]

    results = run_sql(sql, values)

    for row in results:
        atividade = Atividade(row['nome'],
                              row['cod_instrutor'],
                              row['data'],
                              row['duracao'],
                              row['capacidade'],
                              row['cod_tipo_plano'],
                              row['ativo'],
                              row['id_atividade'])
        atividades.append(atividade)
    return atividades

#funcao para cadastrar um instrutor
def new(instrutor):

    sql = "insert into webuser.tb_intrutores (nome, sobrenome, data_nascimento, endereco, telefone) values (%s, %s, %s, %s, %s) RETURNING *;"
    values = [instrutor.nome, instrutor.sobrenome, instrutor.data_nascimento, instrutor.endereco, instrutor.telefone]
    
    results = run_sql(sql, values)

    instrutor.id = results[0]['id_instrutor']

    return instrutor

#funcao para deletar um instrutor
def delete_one(id):

    sql = 'delte from webuser.tb_intrutores where id_instrutor = %s'
    value = [id]

    run_sql(sql, value)

#funcao para editar um instrutor
def edit(instrutor):

    sql = 'update webuser.tb_intrutores set (nome, sobrenome, data_nascimento, endereco, telefone ) = (%s, %s, %s, %s, %s) WHERE id = %s;'
    values = instrutor.nome, instrutor.sobrenome, instrutor.data_nascimento, instrutor.endereco, instrutor.telefone, instrutor.id_instrutor

    run_sql(sql, values)

