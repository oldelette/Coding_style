import subprocess
import sys
import os
from config import *

class Quality:
    
    def __init__(self):
        pass

    """subprocess run test"""
    def judge(self,cmd:str) -> bool:
        try:
            subprocComplete = subprocess.run(
                cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            #print(subprocComplete.stdout.decode("utf-8"))
            return True
        except subprocess.CalledProcessError as err:
            print(err.output.decode("utf-8"))
            return False
    
    def black(self,name):
        command="black --check " + name
        #subprocess.run(command,shell=True)
        status = self.judge(command)
        if not status:
            subprocess.run("black " + name,shell=True)
        return status 
    
    """pylint test"""
    def pylint(self,name:str) -> int:
        command = "pylint " + name
        return self.judge(command)
    
    
    """flake8 test"""
    def flake8(self,name:str) -> int:
        command = "flake8 " + name
        return self.judge(command)
    
    
    """mypy test"""
    def mypy(self,name:str) -> int:
        command = "mypy " + name
        return self.judge(command)
    
    
    def create_dir():
        if os.path.isdir(py_dir) == False:
            os.mkdir(py_dir)
    
    
    def coding_style(self,name_list):
        status=1
        for name in name_list:
            full_name=py_dir+name
            if self.pylint(full_name) and self.flake8(full_name):
                print("pass pylint/flake8 check")
            else:
                print("not pass pylint/flake8 check")
                status=0
        return status


