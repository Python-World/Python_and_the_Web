import subprocess

def fork(): 
    username = input("Your github username: ")
    password = input("Your github password: ")
    repo = input("Name of repo you want to fork: ")
    owner = input("Username of repo owner: ")
    subprocess.run("curl -X POST -u " + username + ":" + password +  " https://api.github.com/repos/" + owner + "/" + repo + "/forks" , shell=True)
    answer = input("Did it fork properly (y/n)? ")
    if answer == "n": fork() 
    clone(username, repo)

def clone(username, repo):

    location = input("Path for cloning repo into (if current current directory press enter): ")
    if len(location):
        subprocess.run("git clone https://github.com/"+ username + "/" + repo + ".git " + location , shell=True)
        answer = input("Did it clone properly (y/n)? ")
        if answer == "n": clone(username, repo) 
    else:
        subprocess.run("git clone https://github.com/"+ username + "/" + repo + ".git" , shell=True)

if __name__ == "__main__":
    fork()
