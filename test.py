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
        test_param = {32.8: [22, 33, 44, 10, 55],
                      28: [20, 22, 21, 33, 44],
                      7.8: [10, 5, 7, 8, 9],
                      0: [0, 0, 0, 0, 0],
                      -12.4: [-1, -21, -3, -17, -20]
                      }
        for k, v in test_param.items():
            result_value = main.avg_from_list(v)
            test_param = k
            self.assertEqual(result_value, test_param)

    def test_type(self):
        test_param = [['22', '33', '44', '10', '55'],
                      ['20', '22', '21', '33', '44'],
                      ['10', '5', '7', '8', '9'],
                      ['0', '0', '0', '0', '0'],
                      ['-1', '-21', '-3', '-17', '-20']]
        for v in test_param:
            result = main.type_values_in_list(v)
            for item in result:
                if type(item) != int:
                    self.assertEqual(result, ValueError)
    def test_value(self):
        test_param = {55: ['22', '33', '44', 'foo', 'ffff']
                      }
        for v in test_param.values():
            result = main.type_values_in_list(v)
            for item in test_param:
                if type(item) != int:
                    self.assertEqual(result, ValueError)

if __name__ == "__main__":
    unittest.main()
