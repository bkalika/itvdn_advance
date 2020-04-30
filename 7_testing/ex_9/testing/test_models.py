import datetime

from models import User


def setup_method(self, method):
    raise ValueError


class TestUserModel:
    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_constructor(self):
        user = User('e@ex.com', 't1', 't2')
        assert user.f_name == 't1'
        assert user.l_name == 't2'
        assert user.email == 'e@ex.com'

    def test_str(self, user):
        pattern = f'User: <{user.id}: {user.get_full_name()}>'
        assert str(user) == pattern.format(id=user.id,
                                           name=user.get_full_name())

    def test_full_name(self, user):
        pattern = '{} {}'
        assert user.get_full_name() == \
            pattern.format(user.f_name, user.l_name)

    def test_list(self):
        assert [1, 2, 3] == [1, 2, 3]

    def test_mocker(self, mocker):
        mocked_dt = mocker.patch('datetime.datetime')
        mocked_dt.now.return_value = 1
        assert datetime.datetime.now() == 1
        assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] == \
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
