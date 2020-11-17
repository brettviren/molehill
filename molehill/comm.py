'''
Things related to communicating with zyre
'''
from pyre import Pyre, PyreEvent
from collections import namedtuple

groups = ['EMPTY', 'BUILT', 'READY', 'RUNNING', 'AVAILABLE', 'BROKEN']


def peer(rolename, partnum):
    peername = "%s-%02d" % (rolename, partnum)
    portnum = 5670 + partnum    # fixme: risking collission!
    print (peername)
    ret = Pyre(peername)
    ret.set_port(bytes(str(portnum).encode("ascii")))
    ret.set_header("role", rolename)
    return ret
