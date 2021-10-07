import logging
import paramiko

hostname = '172.17.0.2'
port = 2222
username = 'test'
password = '123'
CMD="ls"
#CMD="useradd mcleezs"

FORMAT = '[%(asctime)s %(levelname)s]: %(message)s'
logging.basicConfig(level=logging.INFO, filename='log.txt', filemode='w',
	format=FORMAT,
	datefmt='%Y%m%d %H:%M:%S',
	)

def get_ssh_connection(ssh_machine, ssh_username, ssh_password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ssh_machine,port=2222,username=ssh_username, password=ssh_password, timeout=10)
    return client

def run_sudo_command(ssh_username, ssh_password, ssh_machine, command):
    conn = get_ssh_connection(ssh_machine=ssh_machine, ssh_username=ssh_username, ssh_password=ssh_password)
    jobid="None"
    command = "sudo -S -p '' %s" % command
    logging.info("Job[%s]: Executing: %s" % (jobid, command))
    stdin, stdout, stderr = conn.exec_command(command=command)
    stdin.write(ssh_password + "\n")
    stdin.flush()
    stdoutput = [line for line in stdout]
    stderroutput = [line for line in stderr]
    print(stderroutput)
    for output in stdoutput:
        logging.info("Job[%s]: %s" % (jobid, output.strip()))

    logging.debug("Job[%s]:stdout: %s" % (jobid, stdoutput))
    logging.debug("Job[%s]:stderror: %s" % (jobid, stderroutput))
    logging.info("Job[%s]:Command status: %s" % (jobid, stdout.channel.recv_exit_status()))
    if not stdout.channel.recv_exit_status():
        logging.info("Job[%s]: Command executed." % jobid)
        conn.close()
        if not stdoutput:
            stdoutput = True
        return True, stdoutput
    else:
        logging.error("Job[%s]: Command failed." % jobid)
        for output in stderroutput:
            logging.error("Job[%s]: %s" % (jobid, output))
        conn.close()
        return False, stderroutput

def main():
    run_sudo_command(username,password,hostname,CMD)

if __name__ == '__main__':
    main()

