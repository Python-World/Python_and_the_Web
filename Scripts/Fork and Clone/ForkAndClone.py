import subprocess

def fork(username, password, repo, owner): 
    subprocess.run("curl -X POST -u " + username + ":" + password +  " https://api.github.com/repos/" + owner + "/" + repo + "/forks" , shell=True)

def clone(username, repo):

    location = input("Path for cloning repo into (if current current directory press enter): ")
    if len(location):
        subprocess.run("git clone https://github.com/"+ username + "/" + repo + ".git " + location , shell=True)
        answer = input("Did it clone properly (y/n?")
        if answer == "n": clone(username, repo) 
    else:
        subprocess.run("git clone https://github.com/"+ username + "/" + repo + ".git" , shell=True)

if __name__ == "__main__":
    username = input("Your github username: ")
    password = input("Your github password: ")
    owner = input("Name of repo you want to fork: ")
    repo = input("Username of repo owner: ")
    
    fork(username, password, repo, owner)
    clone(username, repo)

