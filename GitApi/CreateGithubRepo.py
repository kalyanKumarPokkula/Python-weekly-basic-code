import requests


def create_github_repo(token, repo_name):
    # API to create a github repository
    url = f"https://api.github.com/user/repos"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    data = {
        "name": repo_name,
        # "description": repo_description,
        "auto_init": False,
        "private": False,
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Repository '{repo_name}' created successfully")
        print(response.json())

    except Exception as e:
        print(f"Error creating repository")
        print(e)


repo_name = input("Enter the repo name : ")
# repo_description = input("Enter the repo description : ")
token = input("Enter the github token : ")

create_github_repo(token, repo_name)
