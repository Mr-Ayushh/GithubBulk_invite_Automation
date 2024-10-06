import requests

# Set your GitHub personal access token for authentication
TOKEN = 'your_personal_access_token_here'  # Replace with your actual token

# Specify your organization name here
ORG_NAME = 'CodeWithTechries'  # Your GitHub organization name

# List of GitHub usernames to invite
usernames_to_invite = [
    'Mr-Ayushh',  # User 1
    'memaxop'     # User 2
]

def invite_user_to_org(username):
    """Send an invitation to a GitHub user to join the organization."""
    api_url = f'https://api.github.com/orgs/{ORG_NAME}/invitations'
    headers = {
        'Authorization': f'token {TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }

    # Get the user ID for the invitee
    try:
        invitee_id = retrieve_user_id(username)
        data = {'invitee_id': invitee_id}

        response = requests.post(api_url, json=data, headers=headers)

        if response.status_code == 201:
            print(f'Invitation sent successfully to {username}!')
        else:
            print(f'Could not invite {username}: {response.json()}')
    except Exception as e:
        print(f'Error while inviting {username}: {e}')

def retrieve_user_id(username):
    """Fetch the user ID from GitHub using the username."""
    api_url = f'https://api.github.com/users/{username}'
    headers = {
        'Authorization': f'token {TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()['id']
    else:
        raise Exception(f'Unable to get user ID for {username}')

# Iterate through each username and send invites
for user in usernames_to_invite:
    invite_user_to_org(user)
