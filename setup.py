from pip.req import parse_requirements
import os
from setuptools import setup


# 依存先が github でも動くように頑張る。

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
entries = list(parse_requirements(path, session=False))
install_reqs = []
dep_links = []

for entry in entries:
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
