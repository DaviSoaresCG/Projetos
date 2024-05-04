import conectores.conector_plano as plano
from database.run_sql import run_sql
from classes.membro import Membro
from classes.atividade import Atividade

#funcao para retornar a lista de membros
def get_all():
     
    membros = []

    sql = 'select * from webuser.tb_membros'

    results = run_sql(sql)

    for row in results:
        tipo_plano = plano.get_one(row["cod_tipo_plano"])

        membro = Membro(row['nome'],
                        row['sobrenome'],
                        row['data_nascimento'],
                        row['endereco'],
                        row['telefone'],
                        row['email'],
                        tipo_plano,
                        row['data_inicio'],
                        row['ativo'],
                        row['id_membro'])
        membros.append(membro)
    return membros

# Função para obter um membro
def get_one(id):

    sql = 'select * from webuser.tb_membros where id_membro = %s'
    values = [id]

    result = run_sql(sql, values)[0]

    if result is not None:
        tipo_plano = plano.get_one(result["cod_tipo_plano"])
        membro = Membro(result['Nome'],
                        result['sobrenome'],
                        result['data_nascimento'],
                        result['endereco'],
                        result['telefone'],
                        result['email'],
                        tipo_plano,
                        result['data_inicio'],
                        result['ativo'],
                        result['id_membro'])
    return membro

# Função para obter a lista de atividades de um membro
def get_activities(user_id):
    atividades = []
    
    sql = 'SELECT * FROM webuser.TB_ATIVIDADES INNER JOIN webuser.TB_AGENDAMENTOS on webuser.TB_ATIVIDADES.id_atividade = webuser.TB_AGENDAMENTOS.cod_atividade where webuser.TB_AGENDAMENTOS.cod_membro = %s'
    
    value = [user_id]

    results = run_sql(sql, value)

    for row in result:
        tipo_plano = plano.get_one(result["cod_tipo_plano"])

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

# Função para retornar todos os membros ativos
def get_all_active():

    membros = []

    sql = 'select * from webuser.tb_membros where ativo = true'

    results = run_sql(sql)

    for row in results:
        tipo_plano = plano.get_one(result["cod_tipo_plano"])

        membro = Membro(row['nome'],
                        row['cod_instrutor'],
                        row['data'],
                        row['duracao'],
                        row['capacidade'],
                        tipo_plano,
                        row['ativo'],
                        row['id_atividade'])
        membros.append(membro)
    return membros

# Função para retornar todos os membros inativos
def get_all_inactive():
    membros = []

    sql = 'select * from webuser.tb_membros where ativo = false'

    results = run_sql(sql)

    for row in results:
        tipo_plano = plano.get_one(result["cod_tipo_plano"])

        membro = Membro(row['nome'],
                        row['cod_instrutor'],
                        row['data'],
                        row['duracao'],
                        row['capacidade'],
                        tipo_plano,
                        row['ativo'],
                        row['id_atividade'])
        membros.append(membro)
    return membros

# Função para cadastrar um novo membro
def new(membro):
    sql = 'INSERT INTO webuser.TB_MEMBROS( nome, sobrenome, data_nascimento, endereco, telefone, email, cod_tipo_plano, data_inicio, ativo ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s ) RETURNING *;'
    values = [membro.nome, membro.sobrenome, membro.data_nascimento, membro.endereco, membro.telefone, membro.email, membro.cod_tipo_plano, membro.data_inicio, membro.ativo]

    result = run_sql(sql)

    membro.id_membro = result[0]['id_membro']

    return membro

# Função para deletar um membro
def delete_one(id):
    
    sql = 'delete from webuser.tb_membro where id_membro = %s'
    values = [id]
    
    run_sql(sql, values)

# Função para atualizar um membro
def edit(membro):
    sql = 'UPDATE webuser.TB_MEMBROS SET ( nome, sobrenome, data_nascimento, endereco, telefone, email, cod_tipo_plano, data_inicio, ativo ) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id_membro = %s;'
    values = [membro.nome, membro.sobrenome, membro.data_nascimento, membro.endereco, membro.telefone, membro.email, membro.cod_tipo_plano, membro.data_inicio, membro.ativo]

    result = run_sql(sql, values)


