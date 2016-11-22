# import importlib
# import json
# import os
# import jsonpickle as jsonpickle
# import pytest
# from fixture.application import Application
#
# fixture = None
# target = None
#
#
# def load_config(file):
#     global target
#     if target is None:
#         config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
#         with open(config_file) as config_file:
#             target = json.load(config_file)
#     return target
#
#
# @pytest.fixture  # Инициализация фикстуры
# def app(request):
#     global fixture
#     browser = request.config.getoption("--browser")
#     web_config = load_config(request.config.getoption("--target"))["web"]
#     if fixture is None or not fixture.is_valid():  # Самый первый раз
#         fixture = Application(browser=browser, base_url=web_config["baseUrl"])
#     fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
#     return fixture
#
#
# @pytest.fixture(scope="session", autouse=True)  # Финализация в конце всех тестов
# def stop(request):
#     def fin():
#         fixture.session.ensure_logout()
#         fixture.destroy()
#
#     request.addfinalizer(fin)
#     return fixture
#
# @pytest.fixture
# def check_ui(request):
#     return request.config.getoption("--check_ui")
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="firefox")
#     parser.addoption("--target", action="store", default="target.json")
#     parser.addoption("--check_ui", action="store_true")
#
#
# def pytest_generate_tests(metafunc):
#     for fixture in metafunc.fixturenames:
#         if fixture.startswith("data_"):
#             testdata = load_from_module(fixture[5:])
#             metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
#         elif fixture.startswith("json_"):
#             testdata = load_from_json(fixture[5:])
#             metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
#
#
# def load_from_module(module):
#     return importlib.import_module("data.%s" % module).testdata
#
#
# def load_from_json(file):
#     with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
#         return jsonpickle.decode(f.read())
#
#
# if __name__ == '__main__':
#     pytest.main()
