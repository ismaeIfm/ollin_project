#!/usr/bin/python
import pxssh

ollin = pxssh.pxssh()

if not ollin.login('ollin.fisica.unam.mx','root'):
    print "ssh session failed longin"
    print str(ollin)
else:
    print "ssh session login successful"

ollin.logout()
#!/usr/bin/python
import pxssh

ollin = pxssh.pxssh()

if not ollin.login('ollin.fisica.unam.mx','root'):
    print "ssh session failed longin"
    print str(ollin)
else:
    print "ssh session login successful"
    master = True

if master == True:
    for i in range(1,11):
        ollin.sendline('ssh root@ollin-'+str(i))
        ollin.prompt()
        print ollin.before
