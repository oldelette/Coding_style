import paramiko
import logging
import pandas as pd

HOSTNAME = "172.17.0.2"
PORT = 2222
USERNAME = "test"
PASSWORD = "123"
labels=["Name","Content"]
#labels=["Name"]

def run_sudo_command(
    ssh_username: str, ssh_password: str, ssh_machine: str, ssh_port: int, command: str
) -> bool:
    # conn = get_ssh_connection(ssh_machine=ssh_machine, ssh_username=ssh_username, ssh_password=ssh_password)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=ssh_machine,
        port=ssh_port,
        username=ssh_username,
        password=ssh_password,
        timeout=10,
    )

    jobid = "None"
    command = "sudo -S -p '' %s" % command
    logging.info("Job[%s]: Executing: %s" % (jobid, command))
    stdin, stdout, stderr = client.exec_command(command=command)
    stdin.write(ssh_password + "\n")
    stdin.flush()
    stdoutput = [str(line) for line in stdout]
    stderrout = [str(line) for line in stderr]
    
    #df1 = pd.DataFrame(stdoutput, columns = labels)
    #print(df1)
    """
    path= "output.txt"
    f = open(path,"w")
    f.writelines(stdoutput)
    f.close()
    #print(stdoutput)
    #print(stderrout)
    """
    filename='savconfig.txt'
    data = pd.read_csv(filename,names=labels,sep=':')
    #data = pd.read_table(filename,names=labels,sep=':')
    print(data)
    print("--" * 20)
    client.close()
    return True if len(stderrout) == 0 else False


def main():
    CMD = "df -h"
    sta = run_sudo_command(USERNAME, PASSWORD, HOSTNAME, PORT, CMD)
    #print(sta)


if __name__ == "__main__":
    main()
