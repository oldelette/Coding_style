import paramiko
import os

# HOSTNAME = os.getenv("HOSTNAME")
# PORT = os.getenv("PORT")
# USERNAME = os.getenv("USERNAME")
# PASSWORD = os.getenv("PASSWORD")

HOSTNAME = "127.0.0.1"
PORT = 49154
USERNAME = "root"
PASSWORD = "root"
ACCOUNT = "mcleezs"

"""
def get_ssh_connection(ssh_username: str, ssh_password: str, ssh_machine: str, ssh_port: int):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ssh_machine,port=ssh_port,username=ssh_username, password=ssh_password, timeout=10)
    return client
"""


def run_sudo_command(cmd: str) -> bool:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=HOSTNAME,
        port=PORT,
        username=USERNAME,
        password=PASSWORD,
        timeout=10,
    )

    # command = "sudo -S -p '' %s" % cmd
    # print(command)
    command = cmd
    stdin, stdout, stderr = client.exec_command(command=command)
    stdin.write(PASSWORD + "\n")
    stdin.flush()
    stdoutput = [str(line) for line in stdout]
    stderrout = [str(line) for line in stderr]
    print("stdout: ", stdoutput)
    print("stderr: ", stderrout)
    print("--" * 20)
    client.close()
    return not bool(stderrout)  # if cmd success,return 1 ; others, return 0


def check(out: int) -> bool:
    return True if bool(out)==run_sudo_command("ls") else False


def cmd_list() -> list:
    create_dir = "mkdir " + ACCOUNT
    create_user = "useradd -p $(echo 'qwe' | openssl passwd -1 -stdin) " + ACCOUNT
    # create_user = "ls"
    check_status = "cat /etc/passwd | grep mcleezs"
    commands = [create_dir, create_user, check_status]
    return commands


def main():  # pragma: no cover
    cmds = cmd_list()
    for cmd in cmds:
        run_sudo_command(cmd)

    #print(check(0))


if __name__ == "__main__":  # pragma: no cover
    main()
