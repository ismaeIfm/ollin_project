#!/usr/bin/python

import pxssh

#Excluir al master indicando en la segunda entrada de la funcion False.
#Incluir al master no indicando nada en la sengunda entrada de la funcion.
 
def executeCommand(command,master = True):

    ollin = pxssh.pxssh()

    if not ollin.login('ollin.fisica.unam.mx','root'):
        print "ssh session failed longin"
        print str(ollin)
    else:
        print "ssh session login successful"


        if master == False:
            for i in range(1,3):
                ollin.sendline('ssh root@ollin-'+str(i))
                ollin.sendline(command)
                ollin.prompt()
                print ollin.before
        else:
            ollin.sendline(command)
            for i in range(1,3):
                ollin.sendline('ssh root@ollin-'+str(i))
                ollin.sendline(command)
                ollin.prompt()
                print ollin.before
                

    ollin.logout()



#executeCommand('ls -a')
#executeCommand('ls -a',False)
