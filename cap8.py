# coding: utf-8

import decimal
import unittest
from unittest import mock


class Column:
    def __init__(self, name, kind, description=""):
        self._name = name
        self._kind = kind
        self._description = description

    @staticmethod
    def validate(kind, data):
        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind == 'numeric':
            try:
                val = decimal.Decimal(data)
            except:
                return False
            return True


class ColumnTest(unittest.TestCase):
    """
    apenas métodos com prefixo 'test_' serão executados pelo main
    """
    def test_validate_bigint(self):
        self.assertTrue(Column.validate('bigint', 100))
        self.assertTrue(not Column.validate('bigint', 10.1))
        self.assertTrue(not Column.validate('bigint', 'texto'))

    def test_validate_numeric(self):
        self.assertTrue(Column.validate('numeric', 10.1))
        self.assertTrue(Column.validate('numeric', 100))
        self.assertTrue(not Column.validate('numeric', 'texto'))

    def test_validate_varchar(self):
        self.assertTrue(Column.validate('varchar', 'texto'))
        self.assertTrue(not Column.validate('varchar', 100))
        self.assertTrue(not Column.validate('varchar', 10.1))


# testando exceção

"""
class DataTableTest(unittest.TestCase):
    def test_add_column_invalid_type_fail(self):
        a_table = DataTable('A')
        error = False
        try:
            a_table.add_column('col', 'invalid')
        except:
            error = True

        if not error:
            self.fail("Chamada não gerou erro, mas deveria")
"""

""""
class DataTableTest(unittest.TestCase):
    def setUp(self):
        self.table = DataTable('A')
        self.addCleanup(self.my_cleanup, ('cleanup executado'))
        self.out_file = open()

    # garantir a execução de limpeza mesmo que haja erro no setUp
    def my_cleanup(self, msg):
        print(msg)

    def test_add_column(self):
        self.assertEqual(0, len(self.table._columns))
        self.table.add_column('BId', 'bigint')
        self.assertEqual(1, len(self.table._columns))
        self.table.add_column('value', 'numeric')
        self.assertEqual(2, len(self.table._columns))
        self.table.add_column('desc', 'varchar')
        self.assertEqual(3, len(self.table._columns))

    def test_add_column_invalid_type(self):
        self.assertRaises(Exception,
        self.table.add_column, ('col', 'invalid'))
"""


BUFF_SIZE = 1024


def download_length(response, output, length):
    times = length / BUFF_SIZE
    if times % BUFF_SIZE > 0:
        times += 1
    for time in range(int(times)):
        output.write(response.read(BUFF_SIZE))
        print('Download %d ' % ((time * BUFF_SIZE)/length)*100)


class DownloadTest(unittest.TestCase):
    def test_download_with_known_length(self):
        response = mock.MagicMock()
        response.read = mock.MagicMock(side_effect=['Data']*2)

        output = mock.MagicMock()
        download_length(response, output, 1025)

        calls = [mock.call(BUFF_SIZE), mock.call(BUFF_SIZE)]

        response.read.assert_has_calls(calls)

        calls = [mock.call('Data'), mock.call('Data')]

        output.write.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()

