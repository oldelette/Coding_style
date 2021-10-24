import os
import re
import sys
import paramiko
#from dataclasses import dataclass
# HOSTNAME = os.getenv("HOSTNAME")
# PORT = os.getenv("PORT")
# USERNAME = os.getenv("USERNAME")
# PASSWORD = os.getenv("PASSWORD")

#@dataclass
class User:
    #hostname: str = "127.0.0.1"
    #port:int = 49153
    #password:str = "root"
    #username:str = "root"
    #account_list:str ="userlist.txt"
    #account:str = "test"
    """
    ssh_info = {
        "hostname": "127.0.0.1",
        "port": 49154,
        "password": "root",
        "username": "root",
        "account_list": "userlist.txt",
        "account": "test",
    } 
    """
    def __init__(self):
        self.hostname: str = "127.0.0.1"
        self.port:int = 49154
        self.password:str = "root"
        self.username:str = "root"
        self.account_list:str ="userlist.txt"
        self.account:str = "test"

    def write_file(self, msg: str):
        path = "output.txt"
        with open(path, "a", encoding="UTF-8") as fout:
            fout.write(msg)
            fout.close()

    def get_ssh_connection(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=self.hostname,
            port=self.port,
            username=self.username,
            password=self.password,
            timeout=10,
        )
        return client

    def run_sudo_command(self, cmd: str) -> bool:
        #client = paramiko.SSHClient()
        #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #client.connect(
        #    hostname=self.hostname,
        #    port=self.port,
        #    username=self.username,
        #    password=self.password,
        #    timeout=10,
        #)
        try:
            client = self.get_ssh_connection()
        except (paramiko.AuthenticationException,
                paramiko.ssh_exception.NoValidConnectionsError): #as e:
            print("NoValidConnectionsError")
            sys.exit()

        command = "sudo -S -p '' %s" % cmd
        print(command)
        command = cmd
        stdin, stdout, stderr = client.exec_command(command=command)
        stdin.write(self.password + "\n")
        stdin.flush()
        stdoutput = [str(line) for line in stdout]
        stderrout = [str(line) for line in stderr]
        print("stdout: ", stdoutput)
        print("stderr: ", stderrout)
        print("--" * 20)
        client.close()
        return not bool(stderrout)  # if cmd success,return 1 ; others, return 0

    def check(self, out: int) -> bool:
        return True if bool(out) == self.run_sudo_command("ls") else False

    def cmd_list(self, accounts: str) -> list:
        create_dir = "mkdir /home/" + self.account
        create_user = (
            "useradd -p $(echo 'qwe' | openssl passwd -1 -stdin) "
            + self.account
        )
        # create_user = "ls"
        check_status = "cat /etc/passwd | grep mcleezs"
        commands = [create_dir, create_user, check_status]
        return commands


def main():  # pragma: no cover
    # cmds = cmd_list()
    use = User()
    infile = "userlist.txt"
    with open(infile, "r", encoding="UTF-8") as fin:
        for line in fin.readlines():
            cmds = use.cmd_list("user1")

    for cmd in cmds:
        use.run_sudo_command(cmd)


if __name__ == "__main__":  # pragma: no cover
    main()
