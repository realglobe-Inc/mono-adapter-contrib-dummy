from setuptools import setup


setup(
    name="sugo-unit-dummy",
    version="0.1",
    packages=["sugo.unit"],
    install_requires=["sugo-unit-lib>=0.1"],
    dependency_links=["git+https://github.com/realglobe-Inc/sugo-unit-lib#egg=sugo_unit_lib-0.1"],
)
