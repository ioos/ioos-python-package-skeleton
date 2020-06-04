from mymodule.mymodule import meaning_of_life, meaning_of_life_url


__all__ = ["mymodule"]

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"
