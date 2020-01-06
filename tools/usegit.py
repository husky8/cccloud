import os
def gitpull(path):
    os.system("cd {}".format(path))
    os.system("git pull")
    return "success"