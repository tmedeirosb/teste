# coding utf-8


class DataTable:
    """
    Representa uma tabela de dados

    Breve descrição sobre o datatable

    Attributes:
        name: Nome da Tabela
        columns: [Lista de Colunas]
        data: [Lista de dados]
    """
    def __init__(self, name):
        """
        Construtor

        :param name: Nome da tabela
        :return:
        """
        self._name = name
        self._columns = []
        self._data = []

    @property
    def data(self):
        return self._data


class Column:
    """
    Representa uma coluna em uma DataTable

    Attributes:
        name: Nome da coluna
        kind: Tipo de dado (varchar, bigint, numeric)
        description: descrição da coluna
    """
    def __init__(self, name, kind, description):
        """
        Construtor

        :param name: nome da coluna
        :param kind:
        :param description:
        :return:
        """
        self._name = name
        self._kind = kind
        self._description = description


class TesteEstatico:
    """
    testando método estático
    """
    def _teste(algo, outro):
        print("Imprima %s e %s" % (algo, outro))

    teste = staticmethod(_teste)

TesteEstatico.teste('thiago', 'medeiros')


class A:
    def run(self):
        print('a')


class B:
    def run(self):
        print('b')


class C(A, B):
    pass


c = C()
c.run()
