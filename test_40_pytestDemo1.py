import pytest


@pytest.fixture()   # для запуска перед каждым тестом
def setup():
    print('\nOnce before every method')


def testmethod1(setup):     # также прописать setup в качестве переменной
    print('Test method 1')


def testmethod2(setup):
    print('Test method 1')