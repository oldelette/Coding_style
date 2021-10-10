"""function"""
import subprocess as sb
import os
from libs.config import PY_DIR


def judge(cmd: str) -> bool:
    """subprocess run test"""
    try:
        sb.run(cmd, shell=True, check=True, stdout=sb.PIPE, stderr=sb.PIPE)
        # print(subprocComplete.stdout.decode("utf-8"))
        return True
    except sb.CalledProcessError as err:
        print(err.output.decode("utf-8"))
        return False


def black(name: str) -> bool:
    """black revised"""
    command = "black --check " + name
    # subprocess.run(command,shell=True)
    status = judge(command)
    if not status:
        sb.run("black " + name, shell=True, check=True)
    return status


def pylint(name: str) -> bool:
    """pylint test"""
    command = "pylint " + name
    return judge(command)


def flake8(name: str) -> bool:
    """flake8 test"""
    command = "flake8 " + name
    return judge(command)


def mypy(name: str) -> bool:
    """mypy test"""
    command = "mypy " + name
    return judge(command)


def create_dir():
    """create directory"""
    if os.path.isdir(PY_DIR) is False:
        os.mkdir(PY_DIR)


def coding_style(name_list):
    """pylint/flake8/mypy"""
    status = 1
    for name in name_list:
        full_name = PY_DIR + name
        if pylint(full_name) and flake8(full_name):
            print("pass pylint/flake8 check")
        else:
            print("not pass pylint/flake8 check")
            status = 0
    return status
