#!/usr/bin/python
import sys, getopt, pexpect, time

def main(argv):
   command = ''
   master = True

   try:
      opts, args = getopt.getopt(argv,"hc:",["command=", "exclude-master"])
   except getopt.GetoptError:
      print 'ollin_script.py -c <command>'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print 'ollin_script.py -c <command>'
         sys.exit()
      elif opt in ("-c", "--command"):
         command = arg + ' &'
      elif opt == "--exclude-master":
         master = False

   ssh = pexpect.spawn('ssh root@ollin.fisica.unam.mx')

   if master:
	ssh.sendline(command)

   ssh.sendline('ssh ollin-1 nohup ' + command)
   ssh.sendline('ssh ollin-2 nohup ' + command)
   ssh.sendline('ssh ollin-3 nohup ' + command)
   ssh.sendline('ssh ollin-4 nohup ' + command)
   ssh.sendline('ssh ollin-5 nohup ' + command)   
   ssh.sendline('ssh ollin-6 nohup ' + command)
   ssh.sendline('ssh ollin-7 nohup ' + command)
   ssh.sendline('ssh ollin-8 nohup ' + command)
   ssh.sendline('ssh ollin-9 nohup ' + command)
   ssh.sendline('ssh ollin-10 nohup ' + command)

   time.sleep(1)

	
if __name__ == "__main__":
   main(sys.argv[1:])
