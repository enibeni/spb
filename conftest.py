# -*- coding: utf-8 -*-

import os
import jsonpickle

import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            print("type of testdata" + str(type(testdata)))
            print(testdata)
            ids = [x for x in testdata]
            print("type of ids" + str(type(ids)))
            print(ids)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "data\\parcel\\%s.json" % file), mode="r", encoding="utf-8") as f:
        return jsonpickle.decode(f.read())