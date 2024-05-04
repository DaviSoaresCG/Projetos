class Atividade:

    def __init__(self, nome, cod_instrutor, data, duracao, capacidade, cod_tipo_plano, ativo, id_atividade = None):
        self.nome = nome
        self.cod_instrutor = cod_instrutor
        self.data = data
        self.duracao = duracao
        self.capacidade = capacidade
        self.cod_tipo_plano = cod_tipo_plano
        self.ativo = ativo
        self.id_atividade = id_atividade