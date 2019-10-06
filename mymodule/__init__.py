from mymodule.mymodule import (meaning_of_life, meaning_of_life_url)
__all__ = ["mymodule"]
from ._version import get_versions
__version__ = get_versions()["version"]
del get_versions
