import requests


def list_github_repositories(token):
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repositories = response.json()
        for repo in repositories:
            print(repo["name"])
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")
        print(response.json())


# Replace 'YOUR_TOKEN' with your GitHub token.
github_token = "YOUR_TOKEN"


list_github_repositories(github_token)
