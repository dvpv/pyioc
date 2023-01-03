from setuptools import find_packages, setup

setup(
    name="pyioc",
    packages=find_packages(include=["pyioc", "pyioc.context"]),
    version="0.0.1",
    description="IoC container for python",
    author="dvpv",
    license="MIT",
    install_requires=["pyyaml"],
)
