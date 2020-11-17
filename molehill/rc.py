'''
molehill RC process
'''
import uuid
import molehill.comm as comm


class RC:
    '''
    An RC process
    '''

    def __init__(self, cfgobj):
        '''
        Create an RC with cfg
        '''
        self.cfg = cfgobj
        self.nodemap = dict()
        self.peer = None
        print(cfgobj)
        for node in cfgobj['nodes']:
            self.nodemap[node['ident']] = dict(spec=node, hist=list())

    def online(self):
        '''
        Bring RC online.

        This blocks.
        '''
        self.peer = comm.peer("RC", self.cfg['partnum'])
        self.peer.start()
        for group in comm.groups:
            self.peer.join(group)

    def run(self):
        '''
        Run the process
        '''
        while True:
            # fixme: put this under a poller
            msg = comm.PyreEvent(self.peer)
            print("See peer: %s" % msg)


def run(cfgobj):
    '''
    The RC process
    '''

    rc = RC(cfgobj)
    rc.online()
    rc.run()
