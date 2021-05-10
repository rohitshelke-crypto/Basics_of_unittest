import unittest  # unitest Module inbuild in Python


class SignupTest(unittest.TestCase):  # Every class should extend i.e Testcase class from Unittest Module

    def test_signupbyEmail(self):
        print("my unitTestcase test_signupbyEmail")

    def test_signupbyPhone(self):
        print("my unitTestcase test_signupbyEmail")

    def test_signubyDevice(self):
        print("my nitTestcase test_signupbyEmail")


if __name__ == "__main__":  # - main module  __name__ - Default module name   __main__ main module
    unittest.main()