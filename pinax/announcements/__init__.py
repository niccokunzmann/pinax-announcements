try:
    from importlib.metadata import version
    __version__ = version("pinax-announcements")
except ImportError:
    import pkg_resources
    __version__ = pkg_resources.get_distribution("pinax-announcements").version
