# vim: set filetype=python ts=2 sw=2 sts=2 expandtab: 
import sys, random, os
sys.dont_write_bytecode = True

### ---------------------------------
# Random Tricks

any = random.choice

between = random.randint

def rseed(seed=1): random.seed(1)

def maybe(): return random.random() > 0.5

def shuffle(lst):
  """Python's default shuffle does 
     not return the changed list"""
  random.shuffle(lst)
  return lst

### ---------------------------------
# Dictionary tricls

def kv(d):
  """Return a string of the dictionary,
     keys in sorted order,
     hiding any key that starts with '_'"""
  return '(' + ', '.join(['%s: %s' % (k, d[k])
                          for k in sorted(d.keys())
                          if k[0] != "_"]) + ')'

class Pretty(object):
  def __repr__(i):
    return i.__class__.__name__ + kv(i.__dict__)

class o(Pretty):
  def __init__(i, **adds): i.__dict__.update(adds)

### ---------------------------------

class lite:
    HEAD  = '\033[95m'
    BLUE  = '\033[94m'
    GREEN = '\033[92m'
    WARN  = '\033[93m'
    FAIL  = '\033[91m'
    END   = '\033[0m'
    BOLD  = '\033[1m'
    ULINE = '\033[4m'