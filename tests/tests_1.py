import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_stats(self):
        res = victory_stats_func()
        self.assertEqual(res, 'yandex')

    def test_set(self):
        res = set_func()
        self.assertEqual(res, {98, 35, 15, 213, 54, 119})

    def test_geo_logs(self):
        answer_1 = [{'visit1': ['Москва', 'Россия']},
                    {'visit3': ['Владимир', 'Россия']},
                    {'visit7': ['Тула', 'Россия']},
                    {'visit8': ['Тула', 'Россия']},
                    {'visit9': ['Курск', 'Россия']},
                    {'visit10': ['Архангельск', 'Россия']}
                    ]
        res_3 = geo_logs_func()
        self.assertEqual(res_3, answer_1)


if __name__ == '__main__':
    unittest.main()
