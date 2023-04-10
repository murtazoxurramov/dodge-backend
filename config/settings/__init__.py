from .base import *
from decouple import config

env_type = config('env_type')

if env_type == 'local':
    from .local import *
else:
    from .production import *
