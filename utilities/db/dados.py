import sqlite3


class MissingMandotoryFieldsException(Exception):
    pass


class CadastroSimplesDB(object):

    # nome do arquivo de dados
    db_datafile = "cadastro.db"

    # unica tabela do nosso banco de dados
    table_name = "cadastro"

    # nomes dos campos da tabela
    # tipos de dados: https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types
    tb_cadastro = ["razaosocial", "cnpj", "inscricao", "logradouro", "estado", "cep", "fone", "fat_logradouro", "fat_estado", "fat_cnpj", "fat_inscricao"]
    tb_cadastro_obr = ["razaosocial", "cnpj"]

    def __init__(self):
        # cria automaticamente a tabela, se ela não existir no banco de dados
        if not self._table_exists():
            self._create_table()

    @property
    def conn(self):
        conn = sqlite3.connect(self.db_datafile, isolation_level=None)
        return conn

    def _table_exists(self):
        with self.conn as conn:
            cur = conn.cursor()
            # conta o numero de tabelas com o nome indicado.
            # fetchone() retorna uma tupla, com um valor (que é a quantidade de tabelas)
            res = cur.execute(f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{self.table_name}';").fetchone()  # retorna (num)
            return res[0] > 0  # se não existe, deve retornar zero

    def _create_table(self):
        with self.conn as conn:
            cur = conn.cursor()
            _fields = ", ".join(self.tb_cadastro)
            cur.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name}({_fields})")
            # a linha acima equivale a:
            # cur.execute("CREATE TABLE cadastro(razaosocial, cnpj, inscricao, logradouro, estado, cep, fone, fat_logradouro, fat_estado, fat_cnpj, fat_inscricao)")

    def table_description(self):
        with self.conn as conn:
            cur = conn.cursor()
            res = cur.execute("pragma table_info('cadastro')").fetchall()
            """ vai retornar uma linha com cada campo correspondendo a uma linha da lista:
                    [(0, 'razaosocial', '', 0, None, 0),
                    (1, 'cnpj', '', 0, None, 0),
                    (2, 'inscricao', '', 0, None, 0),
                    (3, 'logradouro', '', 0, None, 0),
                    (4, 'estado', '', 0, None, 0),
                    (5, 'cep', '', 0, None, 0),
                    (6, 'fone', '', 0, None, 0),
                    (7, 'fat_logradouro', '', 0, None, 0),
                    (8, 'fat_estado', '', 0, None, 0),
                    (9, 'fat_cnpj', '', 0, None, 0),
                    (10, 'fat_inscricao', '', 0, None, 0)]
            """
            return res

    def _delete_table(self):
        with self.conn as conn:
            cur = conn.cursor()
            cur.execute(f"DROP TABLE IF EXISTS {self.table_name}")
            # a linha acima equivale a:
            # cur.execute("CREATE TABLE cadastro(razaosocial, cnpj, inscricao, logradouro, estado, cep, fone, fat_logradouro, fat_estado, fat_cnpj, fat_inscricao)")

    def _check_fields(self, data: dict):
        # check dos campos obrigatórios
        if any([len(data.get(k, "").strip()) == 0 for k in self.tb_cadastro_obr]):
            """
            1- se um campo obrigatorio for None, get() retorna ""
            2- se um campo não for none, mas estiver preenchido somente por espacos, strip() transforma ele em ""
            o teste final verifica se o tamanho da string é maior que zero.
            se alguma das duas condições acima aconteceu, len() retorna 0 e cria uma mensagem de erro !
            """
            raise MissingMandotoryFieldsException(f"Nem todos os campos obrigatórios estão preenchidos. Verifique: {self.tb_cadastro_obr}")
            # return False

        # extra: verificar se cnpj é valido
        # formato: xx.xxx.xxx/xxxx-xx
        # digito verificador

        return True

    def _clean(self, data):
        """ remove os espaços extras (à esquerda ou à direita) dos valores de cada campo
        """
        return [x.strip() if x is not None else x for x in data.values()]

    def insert(self, data: dict):
        self._check_fields(data)

        # todos os campos obrigatórios estao presentes, criamos o INSERT
        _fields = ", ".join(data.keys())
        _entries = ", ".join(["?" for _ in data.keys()])  # entry placeholder
        with self.conn as conn:
            cur = conn.cursor()
            sql = f"INSERT INTO {self.table_name}({_fields}) VALUES({_entries})"
            # print(sql)
            try:
                cur.execute(sql, self._clean(data))
                conn.commit()
            except sqlite3.IntegrityError as err:
                print('sqlite error: ', err.args[0])  # column name is not unique

    def update(self, data: dict):
        self._check_fields(data)

        # todos os campos obrigatórios estao presentes, criamos o INSERT
        _fields = ", ".join([f"{k} = ?" for k in data.keys()])
        with self.conn as conn:
            cur = conn.cursor()
            sql = f"UPDATE {self.table_name} SET {_fields} WHERE cnpj = ?"
            # print(sql)
            try:
                cur.execute(sql, self._clean(data) + [data["cnpj"]])  # adicionar o CNPJ para o WHERE
                conn.commit()
            except sqlite3.IntegrityError as err:
                print('sqlite error: ', err.args[0])  # column name is not unique

    def delete(self, cnpj: str):
        with self.conn as conn:
            cur = conn.cursor()
            sql = f"DELETE FROM {self.table_name} WHERE cnpj = ?"
            # print(sql)
            try:
                cur.execute(sql, [data["cnpj"]])
                conn.commit()
            except sqlite3.IntegrityError as err:
                print('sqlite error: ', err.args[0])  # column name is not unique

    def get(self, cnpj: str):
        with self.conn as conn:
            cur = conn.cursor()
            res = cur.execute(f"SELECT * FROM {self.table_name} WHERE cnpj = ?", [cnpj]).fetchall()
            return {k: v for k, v in zip(self.tb_cadastro, res[0])} if len(res) > 0 else None


if __name__ == '__main__':
    import random
    random.seed(0)  # garante a repeticao

    db = CadastroSimplesDB()

    # inserir dados de teste
    cnpjs = []
    for i in range(10):
        data = {"razaosocial": f"firma_{i + 1:02d}",
                "cnpj": "{:014d}".format(int(random.random() * 1e+14)),
                "logradouro" : "Rua n#{}".format(random.randint(1, 20)),
                "estado": random.choice(["SP", "MG", "RJ", "ES"])
                }
        print(i, ">", data)
        db.insert(data)

        # guarda os CNPJs criados para podermos buscar os dados
        cnpjs.append(data["cnpj"])

    #
    # teste de leitura dos dados
    #
    cnpj = random.choice(cnpjs)
    print(f"CNPJ selecionado: {cnpj}")
    dados_empresa = db.get(cnpj)
    print(dados_empresa)
    """
        {'razaosocial': 'firma_02',
         'cnpj': '25891675029296', 'inscricao': None, 'logradouro': 'Rua n#17', 'estado': 'ES', 'cep': None, 'fone': None,
         'fat_logradouro': None, 'fat_estado': None, 'fat_cnpj': None, 'fat_inscricao': None}
    """

    dados_empresa["cep"] = "22222000"
    dados_empresa["fat_logradouro"] = "mesmo endereço"
    print("Novos dados: {dados_empresa}")
    db.update(dados_empresa)
    print("Updated!")

    dados_empresa = db.get(cnpj)
    print("Do BD:", dados_empresa)

    # remove a table para manter o db limpo
    db._delete_table()
