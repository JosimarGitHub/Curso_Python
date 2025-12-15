import requests

def get_repos_info():
    # Make an API call and check the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")
    
    return r

def get_respose_dict(response):
    # Convert the response object to a dictionary.
    response_dict = response.json()

    return response_dict

def show_repos_info(response_dict):
    print(f"Total de Repositórios: {response_dict['total_count']}")
    print(f"Solicitação Completa: {not response_dict['incomplete_results']}")

def get_repos_dict(response_dict):
    # Explore information about the repositories.
    repo_dicts = response_dict['items']
    print(f"Repositórios retornados: {len(repo_dicts)}")

    return repo_dicts

def show_repos_dict_info(repo_dicts):
    # Examine the first repository.
    i = 0
    for repo_dict in repo_dicts:
        i += 1
        print(f"\nSelected information about {i} repository:") 
        print(f"Name: {repo_dict['name']}") 
        print(f"Owner: {repo_dict['owner']['login']}") 
        print(f"Stars: {repo_dict['stargazers_count']}") 
        print(f"Repository: {repo_dict['html_url']}") 
        print(f"Created: {repo_dict['created_at']}") 
        print(f"Updated: {repo_dict['updated_at']}") 
        print(f"Description: {repo_dict['description']}")