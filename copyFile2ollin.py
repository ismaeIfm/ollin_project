#!/usr/bin/python
import sys, getopt, pexpect, time, subprocess

def main(argv):
   origin = ""
   destination = ""
   master = False
   recursive = ""
   try: 
      opts, args = getopt.getopt(argv,"hro:d:",["origin=", "destination=", "exclude-master"])
   except getopt.GetoptError:
      print 'copyFile2ollin.py -o <origin> -d <destination>'
      print 'For directories add -r'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print 'copyFile2ollin.py -o <origin> -d <destination>'
      	 sys.exit()
      elif opt in ("-o", "--origin"):
         origin = arg
      elif opt in ("-d", "--destination"):
         destination = arg
      elif opt == "--exclude-master":
         master = True
      elif opt == "-r":
         recursive = "-r "
   print "hola"
   subprocess.call(["scp", recursive, origin, "root@ollin.fisica.unam.mx:" +destination])
   print "adios"
   ssh = pexpect.spawn('ssh root@ollin.fisica.unam.mx')

   ssh.sendline('scp ' + recursive + destination + "ollin-1:" + destination + " &")
   ssh.sendline('scp ' + recursive + destination + "ollin-2:" + destination + " &")
   ssh.sendline('scp ' + recursive + destination + "ollin-3:" + destination + " &")
   ssh.sendline('scp ' + recursive + destination + "ollin-4:" + destination + " &")
   ssh.sendline('scp ' + recursive + destination + "ollin-5:" + destination + " &")
   ssh.sendline('scp ' + recursive + destination + "ollin-6:" + destination + " &")
   ssh.sendline('scp ' + recursive + destination + "ollin-7:" + destination + " &")
   ssh.sendline('scp ' + recursive + destination + "ollin-8:" + destination + " &")
   ssh.sendline('scp ' + recursive + destination + "ollin-9:" + destination + " &")
   ssh.sendline('scp ' + recursive + destination + "ollin-10:" + destination + " &")
   
   if master:
      ssh.sendline("rm " + recursive + destination + " &")

   time.sleep(1)

if __name__ == "__main__":
   main(sys.argv[1:])
