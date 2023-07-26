import unittest
from yandex_api import *


class MyTestCase(unittest.TestCase):
    def test_create_folder(self):
        res = create_folder('my_folder')
        self.assertEqual(res, 201, f'Не получилось создать папку')

    def test_check_folder(self):
        res_check = check_folder('my_folder')
        self.assertEqual(res_check, 200, f'Папки не существует')


if __name__ == '__main__':
    unittest.main()
