try:
  from . import base
except ImportError:
  import base

class Grep (base.Base):
    pass

engine_class = Grep
