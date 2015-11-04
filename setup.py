from pip.req import parse_requirements
import os
from setuptools import setup


path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
entries = list(parse_requirements(path, session=False))
install_reqs = [str(entry.req) for entry in entries if entry.req]
dep_links = [str(entry.link) for entry in entries if entry.link]

print(install_reqs)
print(dep_links)

exit()

setup(
    name="sugo-unit-dummy",
    version="0.1",
    packages=["sugo.unit"],
    install_requires=install_reqs,
    dependency_links=dep_links,
)
