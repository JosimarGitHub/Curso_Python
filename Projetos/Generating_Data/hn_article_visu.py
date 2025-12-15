from operator import itemgetter
import requests
import plotly.express as px
import json

# Make an API call, and store the response. 
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

r = requests.get(url)
print(f"Status code: {r.status_code}")

#response_string = json.dumps(response_dict, indent=4)
#print(response_string)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:10]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"Status code: {r.status_code}")
    response_dict = r.json()
    # Build a dictionary for each article.
    submission_dict = {'title' : response_dict['title'],
                       'hn_link' : f"https://news.ycombinator.com/item?id={submission_id}",
                       'comments' : response_dict['descendants'],
                    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

################## Make visualization.########################
comments, links, hover_texts = [], [], []
for submission_dict in submission_dicts:

    comments.append(submission_dict['comments'])
    hover_texts.append(submission_dict['title'])
    link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    links.append(link)

title = "The most active discussions currently on Hacker News" 
labels = {'x': 'Discussions', 'y': 'Coments'}

fig = px.bar(x=links,
            y=comments,
            title=title,
            labels=labels,
            hover_name=hover_texts)

fig.update_layout(title_font_size=28,
                xaxis_title_font_size=20,
                yaxis_title_font_size=20,
                hoverlabel=dict(bgcolor="yellow", font_size=16))

fig.update_traces(marker_color='steelblue', marker_opacity=0.6)

fig.show()

'''for submission_dict in submission_dicts: 
    print(f"\nTitle: {submission_dict['title']}") 
    print(f"Discussion link: {submission_dict['hn_link']}") 
    print(f"Comments: {submission_dict['comments']}")'''
    
