from operator import itemgetter

from plotly.graph_objs import Bar
from plotly import offline

import requests
"""
Combined chapter 17 exercises in this one file 
Misinterpreted README as this API works and the other doesn't so use this for all ch17
"""

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
totalSubmissions = len(r.json())
print(f'Stories returned: {totalSubmissions}')

repo_authors, repo_comments, repo_links = [],[], []

for story in range(0, 30):
    submission_id = submission_ids[story]
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    

    # Kept failing cause descendants key was missing from some responses, so I defaulted the key to 0 so I can use the 0 in visualizations
    keys = ['descendants']
    for key in keys:
        response_dict.setdefault(key, 0)

    repo_authors.append(response_dict['by'])
    author_name = response_dict['by']
    repo_comments.append(response_dict['descendants'])
    repo_links.append(f"<a href='http://news.ycombinator.com/item?id={submission_id}'>{author_name}</a>")

    """
    Don't believe this is needed for the visuals
    submission_dict = {
            'title': response_dict['title'],
            'by': response_dict['by'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants']

            }
    """
    
    """
    Not needed for the visuals
    print(f"\nTitle: {submission_dict['title']}")
    print(f"By: {submission_dict['by']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
    """

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': repo_comments,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.7
}]

my_layout = {
    'title': 'Top Stories\' Authors & Comments on HackerNews',
    'titlefont': {'size': 24},
    'xaxis': {
        'title': 'Author',
        'titlefont': {'size': 20},
        'tickfont': {'size': 10},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 20},
        'tickfont': {'size': 10},            
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_top_stories.html')