#!/usr/bin/env python

import subprocess
import sys

#prueba = subprocess.call(["ssh", "root@ollin.fisica.unam.mx", "nohup", "uname -a"])


sshProcess = subprocess.Popen(['ssh', "root@ollin.fisica.unam.mx"])
#sshProcess.stdin.write("uname -a\n")
#prueba.PIPE.write("ifconfig\n")


#command = sys.argv[1]
#exclude_master = int(sys.argv[2])

#print "command"
exit(0)
