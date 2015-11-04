from pip.req import parse_requirements
import os
from setuptools import setup


path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
install_reqs = [str(req.req) for req in parse_requirements(path, session=False)]


setup(
    name="sugo-unit-dummy",
    version="0.1",
    packages=["sugo.unit"],
    install_requires=install_reqs,
)
