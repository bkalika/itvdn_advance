import unittest
import datetime


class UserTestCase(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.current = datetime.datetime.now()

    @classmethod
    def setUpClass(cls) -> None:
        cls.current_cls = datetime.datetime.now()
        print("setUpClass")

    def tearDown(self) -> None:
        print("tearDown")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_example1(self):
        print(self.current)
        print(self.current_cls)

    def test_ex_2(self):
        print(self.current)
        print(self.current_cls)
