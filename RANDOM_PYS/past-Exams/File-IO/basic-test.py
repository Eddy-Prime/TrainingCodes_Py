import inspect
import pytest
import Grades
from os import path

def has_method(cls, *, method_name, parameter_names=None):
    if parameter_names is None:
        parameter_names = []
    method = getattr(cls, method_name)
    if not inspect.isfunction(method):
        return False
    specs = inspect.getfullargspec(method)
    if specs.args != parameter_names:
        return False
    return True

@pytest.mark.parametrize("kwargs", [
    {
        'method_name' : 'calculate_average',
        'parameter_names' : ['grades'],
    }
])
def test_calculate_avg(kwargs):
    assert has_method(
        Grades,
        **kwargs), f"Method {kwargs['method_name']} is missing or incorrect."

@pytest.mark.parametrize("kwargs", [
    {
        'method_name' : 'highest_scorer',
        'parameter_names' : ['grades'],
    }
])
def test_most_expensive(kwargs):
    assert has_method(
        Grades,
        **kwargs), f"Method {kwargs['method_name']} is missing or incorrect."

@pytest.mark.parametrize("kwargs", [
    {
        'method_name' : 'calculate_stats',
        'parameter_names' : ['input'],
    }
])
def test_calculate_stats(kwargs):
    assert has_method(
        Grades,
        **kwargs), f"Method {kwargs['method_name']} is missing or incorrect."

@pytest.mark.parametrize("filename",['results.txt'])
def test_calculate_stats_results(filename):
    assert path.exists(filename), f"Output file {filename} is missing or incorrectly spelled."

