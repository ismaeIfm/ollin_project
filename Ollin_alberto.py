#!/usr/bin/python
import pxssh

ollin = pxssh.pxssh()

if not ollin.login('ollin.fisica.unam.mx','root'):
    print "ssh session failed longin"
    print str(ollin)
else:
    print "ssh session login successful"

ollin.logout()
