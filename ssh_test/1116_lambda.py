import paramiko
import logging

def execute(
    ssh_username: str, ssh_password: str, ssh_machine: str, ssh_port: int, command: str 
) ->list:
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
    #command = "sudo -S -p '' %s" % command
    #logging.info("Job[%s]: Executing: %s" % (jobid, command))
    stdin, stdout, stderr = client.exec_command(command=command)
    #stdin.write(ssh_password + "\n")
    #stdin.flush()
    stdoutput = [str(line) for line in stdout]
    stderrout = [str(line) for line in stderr]

    return stdoutput


cmd_os = ["cat /etc/os-release | grep ID="]
# cmd_os = ["ls /etc"]

HOSTNAME = "127.0.0.1"
PORT = 49153
USERNAME = "root"
PASSWORD = "root"

lis = execute(USERNAME,PASSWORD,HOSTNAME,PORT,cmd_os[0])
print(lis)                                                                                           
#lis = ['ID=ubuntu']
#lis = ['ID=res']

#test = list(map(lambda x: True if "ubuntu" in x else False,lis))
test = list(map(lambda x: True if "ubuntu" in x else False,lis))
print(test)
