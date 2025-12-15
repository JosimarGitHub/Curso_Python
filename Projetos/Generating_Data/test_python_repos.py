import requests
import function_python_repos
import pytest

def test_get_repos_info():
    response = function_python_repos.get_repos_info()
    assert response.status_code == 200

def test_get_response_dict():
    r = function_python_repos.get_repos_info()
    response_dict = function_python_repos.get_respose_dict(r)

    total_count = response_dict['total_count']
    complete_results = not response_dict['incomplete_results']

    assert total_count > 240
    assert complete_results

def test_get_repos_dict():
    r = function_python_repos.get_repos_info()
    response_dict = function_python_repos.get_respose_dict(r)
    repos_dict = function_python_repos.get_repos_dict(response_dict)

    assert len(repos_dict) == 30

    for repo_dict in repos_dict:
        assert repo_dict['stargazers_count'] > 10000
    
test_get_repos_info()
test_get_response_dict()
test_get_repos_dict()