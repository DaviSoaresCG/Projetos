class Membro:
    
    def __init__(self, nome, sobrenome, data_nascimento, endereco, telefone, email, cod_tipo_plano, data_inicio, ativo, id_membro=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.cod_tipo_plano = cod_tipo_plano
        self.data_inicio = data_inicio
        self.ativo = ativo
        self.id_membro = id_membro