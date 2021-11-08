import unittest
import main


class TestMain(unittest.TestCase):
    def test_min(self):
        test_param = {10: [22, 33, 44, 10, 55],
                      20: [20, 22, 21, 33, 44],
                      5: [10, 5, 7, 8, 9],
                      0: [0, 0, 0, 0, 0],
                      -21: [-1, -21, -3, -17, -20]}
        for k, v in test_param.items():
            result_min, result_max = main.min_max(v)
            test_param = k
            self.assertEqual(result_min, test_param)

    def test_max(self):
        test_param = {55: [22, 33, 44, 10, 55],
                      44: [20, 22, 21, 33, 44],
                      10: [10, 5, 7, 8, 9],
                      0: [0, 0, 0, 0, 0],
                      -1: [-1, -21, -3, -17, -20]
                      }
        for k, v in test_param.items():
            result_min, result_max = main.min_max(v)
            test_param = k
            self.assertEqual(result_max, test_param)
    def test_avrg(self):
        test_param = {20: [10, 15, 20, 25, 30],
                      -20: [-10, -15, -20, -25, -30],
                      0: [0, 0, 0, 0, 0]
                      }
        for k, v in test_param.items():
            result_value = main.avg_from_list(v)
            test_param = k
            self.assertEqual(result_value, test_param)


unittest.main()
