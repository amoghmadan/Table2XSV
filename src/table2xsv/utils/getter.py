from pathlib import Path

import table2xsv


def get_package_path():
    """Get Package Path"""
    package_path = Path(__file__).parent.parent
    return package_path


def get_name():
    """Get Name"""
    return table2xsv.__name__


def get_version():
    """Get Version"""
    return table2xsv.__version__


def get_named_version():
    """Get Named Version"""
    return get_name() + " " + get_version()
