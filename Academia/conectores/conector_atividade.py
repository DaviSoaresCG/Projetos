import conectores.plano as plano
from db.run_sql import run_sql
from classes.atividade import Atividade
from classes.membro import Membro

#listar todas as atividades
def get_all():

    atividades = []

    sql = 'select * from webuser.tb_atividades'

    results = run_sql(sql)

    for row in results:
        tipo_plano = get_one(row['cod_tipo_plano'])

        atividade = Atividade(result['nome'],
                               row['cod_instrutor'],
                               row['data'],
                               row['duracao'],
                               row['capacidade'],
                               tipo_plano,
                               row['ativo'],
                               row['id_atividade'])
        atividades.append(atividade)
    return atividades 

#funcao para obter membros
def get_members(id):       
    membros = []
    
    sql = 'SELECT *FROM webuser.tb_membrosINNER JOIN webuser.tb_agendamentos ON tb_membros.id_membro = webuser.tb_agendamentos.cod_membroWHERE webuser.tb_agendamentos.cod_atividade = %s'
    
    values = [id]

    results = run_sql(sql, values)

    for row in results:
        membro = Membro(row['nome'],
                         row['sobrenome'],
                         row['data_nascimento'],
                         row['endereco'],
                         row['telefone'],
                         row['email'],
                         row['cod_tipo_plano'],
                         row['data_inicio'],
                         row['ativo'],
                         row['id_membro'])
        membros.append(membro)
    return membros

#funcao para obter atividades ativas ordenadas por data
def get_all_active():
    
    atividades = []

    sql = 'select * from webuser.tb_atividades where ativo = true order by data asc'

    results = run_sql(sql)

    for row in results:
        tipo_plano = plano.get_one(row["cod_tipo_plano"])

        atividade = Atividade(row['nome'],
                              row['cod_instrutor'],
                              row['data'],
                              row['duracao'],
                              row['capacidade'],
                              tipo_plano,
                              row['ativo'],
                              row['id_atividade'])
        atividades.append(atividade)
    return atividades

## Função para obter atividades inativas
def get_all_inactive():

    atividades = []

    sql = 'select * from webuser.tb_atividades where ativo = false ORDER BY data ASC'

    results = run_sql(sql)

    for row in results:
        tipo_plano = plano.get_one(row['cod_tipo_plano'])

        atividade = Atividade(row['nome'],
                              row['cod_instrutor'],
                              row['data'],
                              row['duracao'],
                              row['capacidade'],
                              tipo_plano,
                              row['ativo'],
                              row['id_atividade'])
        atividades.append(atividade)
    return atividades

# Função para obter uma atividade ativa
def get_one(id):

    sql = 'select * from webuser.tb_atividades where id_atividade = %s and where ativo = true'
    values = [id]

    result = run_sql(sql, values)

    if result is not None:
        tipo_plano = plano.get_one(result["tipo_plano"])
        
        atividade = Atividade(result["nome"],
                              result["instrutor"],
                              result["data"],
                              result["duracao"],
                              result["capacidade"],
                              tipo_plano,
                              result["ativo"],
                              result["id_atividade"])

    return atividade

#funcao para cadastrar atividade
def new(atividade):

    sql = 'INSERT INTO webuser.tb_atividades( nome, instrutor, data, duracao, capacidade, cod_tipo_plano, ativo ) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *;'
    values = [atividade.nome, atividade.instrutor, atividade.data, atividade.duracao, atividade.capacidade, atividade.cod_tipo_plano, atividade.ativo]

    result = run_sql(sql, values)

    atividade.id = result[0]['id_atividade']

    return atividade

# Função para deletar uma atividade
def delete_one(id):
    sql = 'delete from webuser.tb_atividades where id_atividade = %s'
    value = [id]

    run_sql(sql, value)

# Função para editar uma atividade
def edit(id):
    sql =  'sql = "UPDATE webuser.tb_atividades SET ( nome, cod_instrutor, data, duracao, capacidade, cod_tipo_plano, ativo ) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s;'
    values = [atividade.nome, atividade.cod_instrutor, atividade.data, atividade.duracao, atividade.capacidade, atividade.cod_tipo_plano, atividade.ativo]

    run_sql(sql, values)