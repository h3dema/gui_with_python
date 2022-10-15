import sqlite3


class CadastroSimplesDB(object):

    tb_cadastro = ["razaosocial", "cnpj", "inscricao", "logradouro", "estado",
                   "cep", "fone", "fat_logradouro", "fat_estado", "fat_cnpj", "fat_inscricao"]

    def __init__(self):
        """ cria tabela se não existir """
        pass

    def _create_table(self):
        pass

    def _delete_table(self):
        pass

    def insert(self, data: dict):
        pass

    def update(self, data: dict):
        pass

    def delete(self, cnpj: str):
        pass

    def get_all(self) -> list:
        pass

    def get(self, cnpj: str) -> dict:
        pass

if __name__ == "__main__":

    db = CadastroSimplesDB()
