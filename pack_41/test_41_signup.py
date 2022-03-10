import pytest


@pytest.fixture()   # для запуска перед каждым тестом pytest.yield_fixture не используется уже
def setup():
    print('\nOpening browser to signup')
    yield
    print('\nClosing browser after signup')


def test_signup_email(setup):     # также прописать setup в качестве переменной
    print('This is signup by email')


def test_signup_facebook(setup):
    print('This is signup by facebook')
