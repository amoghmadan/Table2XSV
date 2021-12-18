from pathlib import Path

from table2xsv import __name__, __version__


def get_package_path():
    """Get Package Path"""

    package_path = Path(__file__).parent.parent
    return package_path


def get_name():
    """Get Name"""

    return __name__


def get_version():
    """Get Version"""

    return __version__


def get_named_version():
    """Get Named Version"""

    return get_name() + " " + get_version()
