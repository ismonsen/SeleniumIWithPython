import pytest


@pytest.fixture()   # для запуска перед каждым тестом
def setup():
    print('\nOpening browser to login')
    yield
    print('\nClosing browser after login')


def test_login_email(setup):     # также прописать setup в качестве переменной
    print('This is login by email')


def test_login_facebook(setup):
    print('This is login by facebook')
