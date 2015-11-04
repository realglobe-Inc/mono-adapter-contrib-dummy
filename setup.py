from setuptools import setup

setup(
    name="sugo-unit-dummy",
    version="0.1",
    packages=["sugo.unit"],
    install_requires=[
        "sugo-unit-lib",
    ],
    dependency_links=['http://github.com/realglobe-Inc/sugo-unit-lib/tarball/master#egg=sugo_unit_lib'],
)
