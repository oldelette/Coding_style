import subprocess
import sys
import os

#path = "/home/gavin/gavin/codint_style"

"""subprocess run test"""
def judge(cmd:str) -> int:
    try:
        subprocComplete = subprocess.run(
            cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        print(subprocComplete.stdout.decode("utf-8"))
        return 1
    except subprocess.CalledProcessError as err:
        print(err.output.decode("utf-8"))
        return 0

def black(name):
    command="black --check " + name
    #subprocess.run(command,shell=True)
    status = judge(command)
    if not status:
        subprocess.run("black " + name,shell=True)
    return status 

"""pylint test"""
def pylint(name:str) -> int:
    command = "pylint " + name
    return judge(command)


"""flake8 test"""
def flake8(name:str) -> int:
    command = "flake8 " + name
    return judge(command)


"""mypy test"""
def mypy(name:str) -> int:
    command = "mypy " + name
    return judge(command)

"""
def main():
    dirs = os.listdir(path)
    print("test file: ",dirs[6])
    #print(flake8(dirs[6]))
    #print(mypy(dirs[6]))
    #print(mypy(dirs[6]))
    print(black(dirs[6]))
        


if __name__ == "__main__":
    main()
"""