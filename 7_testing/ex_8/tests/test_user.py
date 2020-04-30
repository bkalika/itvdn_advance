import unittest.mock
import unittest
import models


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.email = 'test@ex.com'
        self.f_name = 'f1'
        self.l_name = 'l1'
        self.user = models.User(
            email=self.email,
            f_name=self.f_name,
            l_name=self.l_name
        )

    def test_constructor(self):
        self.assertEqual(self.user.f_name, self.f_name)
        self.assertEqual(self.user.l_name, self.l_name)
        self.assertEqual(self.user.email, self.email)

    def test_f_name(self):
        expected_result = f'{self.f_name} {self.l_name}'
        full_name = self.user.get_full_name()
        self.assertIsInstance(full_name, str)
        self.assertEqual(full_name, expected_result)

    def test_str(self):
        expected = f'User: <{self.user.id}: {self.user.get_full_name()}>'
        str_value = str(self.user)
        self.assertIsInstance(str_value, str)
        self.assertEqual(str_value, expected)

    @unittest.mock.patch('models.send_mail')
    def test_send_mail(self, mocked_send_mail):
        self.user.send_mail()
        mocked_send_mail.assert_called_once_with(
            self.user.email,
            models.SUBJECT_REGISTRATION.format(name=self.user.get_full_name()),
            models.BODY_REGISTRATION
        )
