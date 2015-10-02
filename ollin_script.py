#!/usr/bin/python
import sys, getopt, os, subprocess

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
         command = arg
      elif opt == "--exclude-master":
         master = False
   
   if master:
      os.system(command)
   for i in range(1, 11):
      subprocess.call(["ssh", "ollin-" + str(i), command])

      


	
if __name__ == "__main__":
   main(sys.argv[1:])
