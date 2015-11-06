from pip.req import parse_requirements
import os
from setuptools import setup


# 依存先が github でも動くように頑張る。

install_reqs = []
dep_links = []


for entry in parse_requirements("requirements.txt", session=False):
    if not entry.req:
        continue
    if not entry.link:
        install_reqs.append(str(entry.req))
        continue

    install_reqs.append(str(entry.req)[::-1].replace("-", ">="[::-1], 1)[::-1])
    dep_links.append(str(entry.link))


setup(
    name="sugo-unit-dummy",
    version="0.1",
    packages=["sugo.unit"],
    install_requires=install_reqs,
    dependency_links=dep_links,
)
