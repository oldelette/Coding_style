import subprocess
import sys
import os
from config import *

"""subprocess run test"""
def judge(cmd:str) -> bool:
    try:
        subprocComplete = subprocess.run(
            cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        #print(subprocComplete.stdout.decode("utf-8"))
        return True
    except subprocess.CalledProcessError as err:
        print(err.output.decode("utf-8"))
        return False

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


def create_dir():
    if os.path.isdir(py_dir) == False:
        os.mkdir(py_dir)


def coding_style(name_list):
    status=1
    for name in name_list:
        full_name=py_dir+name
        if pylint(full_name) and flake8(full_name):
            print("pass coding style check")
        else:
            print("bad coding style")
            status=0
    return status

