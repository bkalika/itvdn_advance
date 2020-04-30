import unittest
from models import User
from utils import send_mail, concat_name, set_user_meta


class UtilsTestCase(unittest.TestCase):

    def test_concat_name(self):
        v1, v2 = 'test1', 'test2'
        result = concat_name(v1, v2)
        expected_result = f'{v1} {v2}'
        self.assertEqual(result, expected_result)

    def test_set_user_meta(self):
        instance = User('test@example.com', '1', '2')
        test_meta = {'test_key': 'test_value'}
        set_user_meta(instance, test_meta)
        self.assertDictEqual(instance.meta, test_meta)
