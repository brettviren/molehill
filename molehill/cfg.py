'''
Provide molehill config handling.
'''
import os
from importlib import import_module
import moo


def load(fname_or_mname):
    '''
    Load a configuration file or module
    '''
    if fname_or_mname.endswith(".json") or fname_or_mname.endswith(".jsonnet"):
        path = os.path.join(os.path.dirname(__file__),
                            "jsonnet-code")
        dat = moo.io.load(fname_or_mname, [path])
        return dat
    mname, aname = fname_or_mname.rsplit('.', 1)
    mod = import_module(mname)
    return getattr(mod, aname).pod()
