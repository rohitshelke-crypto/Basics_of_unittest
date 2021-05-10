import unittest  # unitest Module inbuild in Python


class PaymentreturnTest(unittest.TestCase):  # Every class should extend i.e Testcase class from Unittest Module

    def test_pamenreturntdollar(self):
        print("my unitTestcase test_pamentreturndollar")

    def test_pamentreturnPound(self):
        print("my unitTestcase test_pamentreturnPound")

    def test_pamentreturnRupees(self):
        print("my nitTestcase test_pamentreturnRupees")


if __name__ == "__main__":  # - main module  __name__ - Default module name   __main__ main module
    unittest.main()

