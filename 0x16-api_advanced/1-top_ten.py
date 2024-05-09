import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    if 'error' in data or 'data' not in data:
        print(None)
        return

    posts = data['data']['children']
    for post in posts:
        print(post['data']['title'])

# Example usage
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

