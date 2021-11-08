import paramiko
from dataclasses import dataclass, field

@dataclass
class SSH:

    #hostname = '127.0.0.1'
    hostname: str = field(default = "127.0.0.1")
    #port = 49153
    port:int = field(default=49153)
    #username = 'root'
    username:str = field(default='root')
    #password = 'root'
    password:str = field(default='root')
    #cmd = "ls"
    cmd:str = field(default="ls")
    #cmd = "userdel mcleezs"
    #cmd = "useradd mcleezs"
    #cmd = "cat /proc/version"
        
    def ssh_connect(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.hostname, self.port, self.username, self.password)
        print((self.hostname, self.port, self.username, self.password))
        #command = "sudo -S -p '' %s" % cmd
        stdin, stdout, stderr = client.exec_command(command=self.cmd)
        stdin.write(self.password + "\n")
        stdin.flush()

        stdoutput = [line for line in stdout]
        stderrp = [line for line in stderr]
        
        print("stdoutput: ", stdoutput)
        print("stderroutput: ",stderrp)
        print("--"*20)
        
        client.close()

def main():
    myssh = SSH()
    myssh.ssh_connect()

if __name__ == "__main__":
    main()
