from setuptools import setup

setup(
    name="sugo-unit-dummy",
    version="0.1",
    packages=["sugo.unit"],
    install_requires=[
        "sugo-unit-base",
    ],
    dependency_links=[
        'git+https://github.com/realglobe-Inc/sugo-unit-base#egg=sugo_unit_base',
    ]
)
