import pytest


@pytest.fixture()   # для запуска перед каждым тестом pytest.yield_fixture не используется уже
def setup():
    print('\nThis is a message before')
    yield
    print('\nThis is a message after')


def testmethod1(setup):     # также прописать setup в качестве переменной
    print('Test method 1')


def testmethod2(setup):
    print('Test method 1')
