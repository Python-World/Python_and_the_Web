import requests
import json

# Function to call API for details of the User.


def findUserInfo(username):
    url = 'https://api.github.com/users/'+username
    html = requests.get(url)
    return json.loads(html.text)

# Some data is not provided by the user, so this error has to be managed


def getField(key, dic):
    if dic[key] is None:
        return 'Not Available'
    else:
        return dic[key]


if __name__ == "__main__":
    username = input('Enter the Username: ')
    userDetails = findUserInfo(username)
    if 'message' in userDetails.keys():
        print('Not Found')
        exit()
    else:
        print('** Name **\n'+userDetails['name'], '\n')
        print('** About **\n')
        print('Bio: ', getField('bio', userDetails))
        print('E-mail: ', getField('email', userDetails))
        print('Location: ', getField('location', userDetails), '\n')
        print('** Profile Details **\n')
        print('Public Repositories: ', userDetails['public_repos'])
        print('Public Gists: ', userDetails['public_gists'])
        print('Followers: ', userDetails['followers'])
        print('Following: ', userDetails['following'])
