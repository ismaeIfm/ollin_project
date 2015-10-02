#!/usr/bin/python

import sys, getopt, subprocess

def main(argv):
   origin = ""
   destination = ""
   recursive = False
   try: 
      opts, args = getopt.getopt(argv,"hro:d:",["origin=", "destination="])
   except getopt.GetoptError:
      print 'copyFile2ollin.py -o <origin> -d <destination>'
      print 'For directories add -r'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print 'copyFile2ollin.py -o <origin> -d <destination>'
         print 'copyFile2ollin.py -o <origin> -d <destination>'
      	 sys.exit()
      elif opt in ("-o", "--origin"):
         origin = arg
      elif opt in ("-d", "--destination"):
         destination = arg 
      elif opt == "-r":
         recursive = True

   if recursive:
      for i in range(1, 11):
         subprocess.call(["scp","-r", origin, "ollin-" + str(i) + ":" + destination])
   else:
      for i in range(1, 11):
         subprocess.call(["scp", origin, "ollin-" + str(i) + ":" + destination])















   








if __name__ == "__main__":
   main(sys.argv[1:])
