'''
Make a single PROC example config
'''

import molehill as mhs

config = mhs.SSOT(
    nodes=mhs.Nodes([
        mhs.Node(ident="node1",
                 role="lonely",
                 slotspec="*",
                 ports=(),
                 app="sleep 10",
                 commands=(),
                 )
    ]),
    slots=mhs.Slots([
        mhs.Slot(ident="localslot1",
                 hostname="localhost",
                 ipaddress="127.0.0.1",
                 zone="any"),
    ]));
