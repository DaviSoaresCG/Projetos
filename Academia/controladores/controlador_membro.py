# Imports
from flask import render_template, request, redirect
from flask import Blueprint
from classes.membro import Membro
import conectores.conector_membro as conector_membro
import conectores.conector_plano as conector_plano

# Cria o blueprint (instância da classe)
membros_blueprint = Blueprint("membros", __name__)

# Rota para index.html para buscar membros ativos
@membros_blueprint.route("/membros")
def membros_index():
    membros = conector_membro.get_all_active()
    return render_template('/membros/index.html' , membros = membros, title="Membros Ativos")

# Rota para index.html para buscar membros inativos
@membros_blueprint.route('/membros/inativo')
def membros_inativos():
    membros = conector_membro.get_all_inactive();
    return render_template('/membros/index.html', membros = membros, title="Membros Inativos")

# Rota para a página de novo membro
@membros_blueprint.route("/membros/novo")
def novo_membro():
    tipos_planos = conector_plano.get_all()
    return render_template("membros/novo.html", tipos_planos = tipos_planos, title = "Novo Membro")


 # Rora para o POST de criação
@membros_blueprint.route('/membros/novo', methods=['POST'])
def cadastra_membro():    
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    data_nascimento = request.form['data_nascimento']
    email = request.form['email']
    endereco = request.form['endereco']
    telefone = request.form['telefone']
    ativo = request.form['ativo']
    tipo_plano = request.form['tipo_plano']  # Corrigido
    data_inicio = request.form['data_inicio']  # Adicionado

    plano = conector_plano.get_one(tipo_plano)

    membro_novo = Membro(nome, sobrenome, data_nascimento, endereco, telefone, email, plano, data_inicio, ativo)
    conector_membro.new(membro_novo)
    return redirect("/membros")

# Rota para edição
@membros_blueprint.route('/membros/<id>/edit')
def edita_membro(id):
    membro = conector_membro.get_one(id)
    tipos_planos = conector_plano.get_all()
    return render_template("/membros/editar.html", membro = membro, tipos_planos = tipos_planos, title = "Editar Detalhes do Membro")

#rota para edição POST
@membros_blueprint.route('/membros/<id>', methods=['POST'])
def atualiza_membro(id):
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    data_nascimento = request.form["data_nascimento"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    endereco = request.form["endereco"]
    tipo_plano = request.form["tipo_plano"]
    data_inicio = request.form["data_inicio"]
    ativo = request.form["ativo"]
    plano = conector_plano.get_one(tipo_plano)
    membro_atualizado = Membro(nome, sobrenome, data_nascimento, endereco, telefone, email, plano, data_inicio, ativo, id)
    conector_membro.edit(membro_atualizado)
    return redirect("/membros")

# Rota para mostrar detalhes
@membros_blueprint.route("/membros/<id>")
def mostra_detalhes(id):
    membro = conector_membro.get_one(id)
    atividades_agendadas = conector_membro.get_activities(id)
    tipo_plano = conector_plano.get_one(membro.cod_tipo_plano)
    return render_template("/membros/mostrar.html", membro = membro, tipo_plano = tipo_plano, atividades_agendadas = atividades_agendadas, title = "Mostrar Detalhes")


# Rota para deletar
@membros_blueprint.route("/membros/<id>/delete")
def deleta_membro(id):
    conector_membro.delete_one(id)
    return redirect("/membros")