import requests
import plotly.express as px

# Make an API call and check the response.

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)

# Convert the response object to a dictionary.
response_dict = r.json()

# Explore information about the repositories.
repo_dicts = response_dict['items']
repo_stars, repo_links, hover_texts = [], [], []

for repo_dict in repo_dicts:

    repo_stars.append(repo_dict['stargazers_count'])
    
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

    repo_link = f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}</a>"
    repo_links.append(repo_link)

################## Make visualization.########################
title = "Most-Starred Python Projects on GitHub" 
labels = {'x': 'Repository', 'y': 'Stars'}

fig = px.bar(x=repo_links,
            y=repo_stars,
            title=title,
            labels=labels,
            hover_name=hover_texts)

fig.update_layout(title_font_size=28,
                xaxis_title_font_size=20,
                yaxis_title_font_size=20)

fig.update_traces(marker_color='steelblue', marker_opacity=0.6)

fig.show()

