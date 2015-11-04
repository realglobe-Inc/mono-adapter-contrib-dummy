from setuptools import setup

setup(
    name="sugo-unit-dummy",
    version="0.1",
    packages=["sugo.unit"],
    install_requires=["sugounitlib"],
    dependency_links=["http://github.com/realglobe-Inc/sugo-unit-lib/tarball/master#egg=sugounitlib"],
)
