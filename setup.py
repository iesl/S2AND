import re
import setuptools
from setuptools import setup, find_namespace_packages
from os import path

requirements_file = path.join(path.dirname(__file__), "requirements.in")
requirements = [r for r in open(requirements_file).read().split("\n") if not re.match(r"^\-", r)]

setup(
    name="s2and",
    version="0.1",
    url="https://github.com/iesl/S2AND",
    # packages=setuptools.find_packages(),
    # packages=find_namespace_packages(where='src'),
    # package_dir={"": "src"},
    install_requires=requirements,  # dependencies specified in requirements.in
)
