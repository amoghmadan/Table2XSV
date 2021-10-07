from pathlib import Path
from setuptools import setup

README: Path = Path(__file__).resolve().parent.parent / "README.md"

setup(long_description=README.read_text())
