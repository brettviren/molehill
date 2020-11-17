'''
The molehill module.
'''
import moo
from .version import version
from .cfg import load

__version__ = version

# load in schema types
for one in load("molehill-schema.jsonnet"):
    moo.otypes.make_type(**one)
