import paramiko

hostname = '172.17.0.2'
port = 2222
username = 'test'
password = '123'
cmd = "ls"
#cmd = "userdel mcleezs"
#cmd = "useradd mcleezs"
#cmd = "cat /proc/version"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password)
command = "sudo -S -p '' %s" % cmd
stdin, stdout, stderr = client.exec_command(command=command)
stdin.write(password + "\n")
stdin.flush()

stdoutput = [line for line in stdout]
#stdinput = [line for line in stdin]
stderrp = [line for line in stderr]

print("stdoutput: ", stdoutput)
print("stderr: ", stderrp)
print("stderroutput: ",stderrp)
print("--"*20)

client.close()

